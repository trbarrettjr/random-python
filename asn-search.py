#!/usr/bin/python3
import re
import sys
import socket

###
# This program searches RADb for the IP's associated with the
# ASN's.  I use this tool to filter my internet to prevent my
# kids from connecting to Roblox unless I tell say they could.
#
# SPDX-License-Identifier: MIT
###

def main():
    asn = sys.argv[1].upper()
    if asn == '':
        asn = input("ASN Number to Search? ").upper()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(('whois.radb.net', 43))

    query = f"-i origin {asn}\r\n"
    sock.sendall(query.encode('utf-8'))

    response = b""
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data

    sock.close()

    match = re.findall(r'route:\s+([\w.\/]+)', response.decode())

    match.sort()

    if match:
        for i in match:
            print(i)
    
if __name__ == "__main__":
    main()