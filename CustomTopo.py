'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment 2

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta, Muhammad Shahbaz
'''

from mininet.topo import Topo

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        core = self.addSwitch('c1')
        for i in range(fanout):
            agg = self.addSwitch('a%d' %(i+1))
            self.addLink(core,agg,**linkopts1)
            for j in range(fanout):
                edge = self.addSwitch('e%d' %(i*fanout+j+1))
                self.addLink(agg,edge,**linkopts2)
                for k in range(fanout):
                    h = self.addHost('h%d' %(i*fanout*fanout+j*fanout+k+1))
                    self.addLink(h,edge,**linkopts3)


topos = { 'custom': ( lambda: CustomTopo() ) }
