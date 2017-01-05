#!/bin/python

from scapy.all import *
from scapy.layers.dot15d4 import *

# Configuration
interface = 'monitor0'

# TODO
# Security header
# Frame with FCS done in scapy?


# Frames
fcf = Dot15d4()
data = Dot15d4Data(dest_panid=0xbeef, dest_addr=0x0005, src_panid=0xbeef, src_addr=0x0004)
ack = Dot15d4Ack() # Really no args needed? Ack contains 53 zeros as paylaod. Needed to set len?
beacon = Dot15d4Beacon(src_panid=0xbeef, src_addr=0x0004) #Src and dest address are mixed up
cmd = Dot15d4Cmd(dest_panid=0xbeef, dest_addr=0x0005, src_panid=0xbeef, src_addr=0x0004)

cmd_coord_realign = Dot15d4CmdCoordRealign()
cmd_assoc_req = Dot15d4CmdAssocReq()
cmd_assoc_resp = Dot15d4CmdAssocResp()
cmd_disassoc = Dot15d4CmdDisassociation()
cmd_panid_conflict = Dot15d4CmdPanIdConflict()
cmd_orphan = Dot15d4CmdOrphan()
cmd_gts_req = Dot15d4CmdGTSReq()


frame_data = fcf/data/"foobar"
frame_ack = fcf/ack
frame_beacon = fcf/beacon

frame_cmd_assoc_req = fcf/cmd/cmd_assoc_req
frame_cmd_assoc_resp = fcf/cmd/cmd_assoc_resp
frame_cmd_disassoc = fcf/cmd/cmd_disassoc
frame_cmd_panid_conflict = fcf/cmd/cmd_panid_conflict
frame_cmd_orphan = fcf/cmd/cmd_orphan
frame_cmd_coord_realign = fcf/cmd/cmd_coord_realign
frame_cmd_gts_req = fcf/cmd/cmd_gts_req

#raw_input("\nPress enter to start\n")

#sendp(frame, iface=interface, inter=0.100, loop=1)
frame_data.show()
sendp(frame_data, iface=interface)

frame_ack.show()
sendp(frame_ack, iface=interface)

frame_beacon.show()
sendp(frame_beacon, iface=interface)

frame_cmd_assoc_req.show()
sendp(frame_cmd_assoc_req, iface=interface)

frame_cmd_assoc_resp.show()
sendp(frame_cmd_assoc_resp, iface=interface)

frame_cmd_disassoc.show()
sendp(frame_cmd_disassoc, iface=interface)

frame_cmd_panid_conflict.show()
sendp(frame_cmd_panid_conflict, iface=interface)

frame_cmd_orphan.show()
sendp(frame_cmd_orphan, iface=interface)

frame_cmd_coord_realign.show()
sendp(frame_cmd_coord_realign, iface=interface)

frame_cmd_gts_req.show()
sendp(frame_cmd_gts_req, iface=interface)
