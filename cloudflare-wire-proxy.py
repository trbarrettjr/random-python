#!/usr/bin/python3
import socket
import requests

# SPDX-License-Identifier: MIT

CLOUDFLARE_DOH = "https://1.1.1.2/dns-query"

def forward_to_doh(dns_query_bytes):
    headers = {
        "Content-Type": "application/dns-message",
        "Accept": "application/dns-message"
    }
    r = requests.post(CLOUDFLARE_DOH, headers=headers, data=dns_query_bytes)
    r.raise_for_status()
    return r.content # raw DNS wire-format response

def start_dns_proxy():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 53))

    try:
        while True:
            data, addr = sock.recvfrom(512)
            response = forward_to_doh(data)
            sock.sendto(response, addr)
            print(f"Request from {addr}")
    except KeyboardInterrupt:
        print("... Exiting ...")
    finally:
        sock.close()
        print("... Socket Closed ...")

if __name__ == "__main__":
    start_dns_proxy()
