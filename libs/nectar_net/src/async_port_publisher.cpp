#include "nectar_net/async_port_publisher.h"
#include <condition_variable>
#include <mutex>
#include <thread>

namespace nectar::net {
struct AsyncPortPublisher::State {
    std::mutex mutex;
    std::condition_variable wake;
    bool stop=false, ready=false, failed=false, tickRequested=false;
    std::uint64_t now=0, submitted=0;
    PublishResult result;
};
AsyncPortPublisher::AsyncPortPublisher(PublisherBackends backends,std::uint16_t port,bool includeLan)
    : mState(std::make_shared<State>()) {
    auto state=mState;
    std::thread([state,backends=std::move(backends),port,includeLan]() mutable {
        // Publisher is constructed/destroyed HERE: discovery, renewals and
        // lease cleanup must never block the UI/game thread, even on cancel.
        PortPublisher publisher(std::move(backends));
        try {
            auto result=publisher.publish(port,7200,includeLan);
            {
                std::lock_guard<std::mutex> lock(state->mutex);
                if(state->stop)return;
                state->result=result;state->ready=true;
            }
            for(;;) {
                std::uint64_t now;
                {
                    std::unique_lock<std::mutex> lock(state->mutex);
                    state->wake.wait(lock,[&]{return state->stop||state->tickRequested;});
                    if(state->stop)return;
                    now=state->now;state->tickRequested=false;
                }
                if(publisher.maintain(now,result)) {
                    std::lock_guard<std::mutex> lock(state->mutex);
                    if(state->stop)return;
                    state->result=result;state->ready=true;
                }
            }
        } catch(...) {
            std::lock_guard<std::mutex> lock(state->mutex);
            if(!state->stop){state->failed=true;state->ready=true;}
        }
    }).detach(); // shared State and publisher outlive the owning room safely
}
AsyncPortPublisher::~AsyncPortPublisher() {
    std::lock_guard<std::mutex> lock(mState->mutex);
    mState->stop=true;mState->wake.notify_one();
}
bool AsyncPortPublisher::take(PublishResult& result,bool& failed) {
    std::lock_guard<std::mutex> lock(mState->mutex);
    if(!mState->ready)return false;
    result=mState->result;failed=mState->failed;mState->ready=false;return true;
}
void AsyncPortPublisher::tick(std::uint64_t nowMs) {
    std::lock_guard<std::mutex> lock(mState->mutex);
    if(mState->stop||mState->failed)return;
    if(mState->submitted && nowMs>=mState->submitted && nowMs-mState->submitted<1000)return;
    mState->submitted=nowMs;mState->now=nowMs;mState->tickRequested=true;mState->wake.notify_one();
}
} // namespace nectar::net
