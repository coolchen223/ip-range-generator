#!/usr/bin/env python
# Script to take in a subnet and prune out the unnecessary IPs for Nessus purposes
# Written by Samuel Zhu

import sys
import socket
from netaddr import *

def real_range(subnet, debug):
    ip_range = IPNetwork(subnet)
    ip_list = list(ip_range) # Creates a list of all IPs in the range given.
    ret = []
    if debug:
        print "Looking at %s (%s addresses)..." % (subnet, len(ip_list))
    for i in ip_list:
        try:
            if debug:
                print "---"
                print "%s" % i
            name = socket.gethostbyaddr(str(i))[0]
            if debug:
                print name
            if "inr" in name:
                raise
            elif "ishmael" in name:
                raise
            else:
                if debug:
                    print "hostname valid!"
                ret.append(i)
        except:
            if debug:
                print "hostname not valid!"
            # If it's an end of the list, assume that it's not active and cut it out.
            # If it's in the middle of the range, then it's more likely a connection error and it won't matter
            # if we cut it out.

    return str(ret[0]) + "-" + str(ret[-1])

debug = False
for a in sys.argv:
    if 'debug' in a:
        print "DEBUG ON"
        debug = True
        
f = open(sys.argv[-1], 'r')

for line in f:
    print real_range(line, debug)

