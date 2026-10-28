#include "nectar_net/sim_network.h"
#include <cstdio>
using namespace nectar::net;
int main() {
    SimulatedNetwork net(42); auto host=net.createHost(); auto guest=net.createGuest();
    if (!host->listen({"",1}) || !guest->connect({"",1})) return 1;
    TransportEvent event; while(host->poll(event)){} while(guest->poll(event)){}
    LinkConditions impaired; impaired.lossPerMille=1000; impaired.reliableLossDelayMs=200;
    net.setHostToGuest(impaired);
    const std::uint8_t first=1, second=2;
    if(!host->send(Delivery::ReliableOrdered,&first,1)) return 1;
    net.setHostToGuest({});
    if(!host->send(Delivery::ReliableOrdered,&second,1)) return 1;
    net.advance(199); if(guest->poll(event)) return 2;
    net.advance(200);
    if(!guest->poll(event)||event.payload.size()!=1||event.payload[0]!=1) return 3;
    if(!guest->poll(event)||event.payload.size()!=1||event.payload[0]!=2) return 4;
    if(guest->poll(event)) return 5;
    std::puts("PASS delayed reliable packet holds later reliable packets in order");
}
