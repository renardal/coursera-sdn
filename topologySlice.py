'''
Coursera:
- Software Defined Networking (SDN) course
-- Network Virtualization

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta
'''

from pox.core import core
from collections import defaultdict

import pox.openflow.libopenflow_01 as of
import pox.openflow.discovery
import pox.openflow.spanning_tree

from pox.lib.revent import *
from pox.lib.util import dpid_to_str
from pox.lib.util import dpidToStr
from pox.lib.addresses import IPAddr, EthAddr
from collections import namedtuple
import os

log = core.getLogger()


class TopologySlice (EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Slicing Module")
        
        
    """This event will be raised each time a switch will connect to the controller"""
    def _handle_ConnectionUp(self, event):
        
        # Use dpid to differentiate between switches (datapath-id)
        # Each switch has its own flow table. As we'll see in this 
        # example we need to write different rules in different tables.
        dpid = dpidToStr(event.dpid)
        log.debug("Switch %s has come up.", dpid)
        
        """ Add your logic here """
        if dpid == '00-00-00-00-00-01':
# install flow for Upper Slice S1 
            msg_uss131 = of.ofp_flow_mod()
            msg_uss131.match.in_port = 3
            msg_uss131.actions.append(of.ofp_action_output(port = 1))
            event.connection.send(msg_uss131)

# install flow for Upper Slice S1 
            msg_uss113 = of.ofp_flow_mod()
            msg_uss113.match.in_port = 1
            msg_uss113.actions.append(of.ofp_action_output(port = 3))
            event.connection.send(msg_uss113)
# install flow for lower slice s1 
            msg_lss142 = of.ofp_flow_mod()
            msg_lss142.match.in_port = 4
            msg_lss142.actions.append(of.ofp_action_output(port = 2))
            event.connection.send(msg_lss142)
# install flow for lower slice s1 
            msg_lss124 = of.ofp_flow_mod()
            msg_lss124.match.in_port = 2
            msg_lss124.actions.append(of.ofp_action_output(port = 4))
            event.connection.send(msg_lss124)
        elif dpid == '00-00-00-00-00-04':
# install flow for upper slice s4 
            msg_uss413 = of.ofp_flow_mod()
            msg_uss413.match.in_port = 1
            msg_uss413.actions.append(of.ofp_action_output(port = 3))
            event.connection.send(msg_uss413)
# install flow for upper slice s4 
            msg_uss431 = of.ofp_flow_mod()
            msg_uss431.match.in_port = 3
            msg_uss431.actions.append(of.ofp_action_output(port = 1))
            event.connection.send(msg_uss431)
# install flow for lower slice s4 
            msg_lss424 = of.ofp_flow_mod()
            msg_lss424.match.in_port = 2
            msg_lss424.actions.append(of.ofp_action_output(port = 4))
            event.connection.send(msg_lss424)
# install flow for lower slice s4 
            msg_lss442 = of.ofp_flow_mod()
            msg_lss442.match.in_port = 4
            msg_lss442.actions.append(of.ofp_action_output(port = 2))
            event.connection.send(msg_lss442)
        elif dpid == '00-00-00-00-00-02' :

            msg_s212 = of.ofp_flow_mod()
            msg_s212.match.in_port = 1
            msg_s212.actions.append(of.ofp_action_output(port = 2))
            event.connection.send(msg_s212)

            msg_s221 = of.ofp_flow_mod()
            msg_s221.match.in_port = 2
            msg_s221.actions.append(of.ofp_action_output(port = 1))
            event.connection.send(msg_s221)


        elif dpid == '00-00-00-00-00-03' :

            msg_s312 = of.ofp_flow_mod()
            msg_s312.match.in_port = 1
            msg_s312.actions.append(of.ofp_action_output(port = 2))
            event.connection.send(msg_s312)

            msg_s321 = of.ofp_flow_mod()
            msg_s321.match.in_port = 2
            msg_s321.actions.append(of.ofp_action_output(port = 1))
            event.connection.send(msg_s321)


def launch():
    # Run spanning tree so that we can deal with topologies with loops
    pox.openflow.discovery.launch()
    pox.openflow.spanning_tree.launch()

    '''
    Starting the Topology Slicing module
    '''
    core.registerNew(TopologySlice)
