#pragma once
#include "nectar_net/port_publisher.h"
#include <memory>

namespace nectar::net {
// Router I/O only. No transport, game, room code or credentials on this worker.
// Stop is nonblocking; an in-flight bounded router operation finishes and its
// lease is removed on the same worker. Each instance owns a separate mailbox.
class AsyncPortPublisher {
public:
    AsyncPortPublisher(PublisherBackends backends, std::uint16_t port, bool includeLan);
    ~AsyncPortPublisher();
    AsyncPortPublisher(const AsyncPortPublisher&) = delete;
    AsyncPortPublisher& operator=(const AsyncPortPublisher&) = delete;
    bool take(PublishResult& result, bool& failed);
    void tick(std::uint64_t nowMs);
private:
    struct State;
    std::shared_ptr<State> mState;
};
} // namespace nectar::net
