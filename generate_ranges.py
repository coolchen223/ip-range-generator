#!/usr/bin/env python
# Script to take in a subnet and prune out the unnecessary IPs for Nessus purposes
# Written by Samuel Zhu

import socket
import sys

def gen_range(subnet):
    ip_addr = subnet.split("/")[0] #split input on subnet slash
    ip_addr = ".".join(ip_addr.split(".")[:-1]) + ".2"
    #ip_addr = ip_addr[:-1] + "2"   #grab everything except the last digit (works on /24 subnets)


    try:
        hostname = socket.gethostbyaddr(ip_addr)[0]
        ret = ip_addr[:-1] + "4" if "inr" in hostname else ip_addr #fancy ternary statement to put correct start of range
    except:
        ret = ip_addr

    ip_addr = ip_addr[:-1] + "254"
    try:
        hostname = socket.gethostbyaddr(ip_addr)[0]
        ret += "-" + ip_addr[:-3] + "253" if "ishmael" in hostname else "-" + ip_addr #other fancy ternary statement
    except:
        ret += "-" + ip_addr
    return ret

f = open(sys.argv[1], 'r')

for line in f:
    print gen_range(line)

