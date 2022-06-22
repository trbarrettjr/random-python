#!/usr/bin/env python3
import http.client
import base64
import json
import pprint

"""This is to get your tailnet devices and deliver a JSON and Python Library to your device"""

key = "tskey-API_KEY_GOES_HERE" + ":" # It may not be safe to store credentials here
auth_obj = base64.b64encode(key.encode()) # This will automatically encode for HTTP Header

def main():
    header = {
        "User-agent": "test-agent/1.0.0 tailnet", # Be nice and put some contact info in case your agent goes off the rails.
        "Authorization": "Basic %s" % auth_obj.decode(), # Authenticate!
    }
    conn = http.client.HTTPSConnection("api.tailscale.com")
    conn.request("GET", "/api/v2/tailnet/tailnet/devices", None, header) # Replace tailnet with your tailnet

    response = conn.getresponse().read().decode() # File-like object that has to be decoded.
    response = json.loads(response) # Load the JSON response into data that Python can read

    pprint.pprint(response) # pprint will make it pretty to view dictionaries.

if __name__ == "__main__":
    main()
