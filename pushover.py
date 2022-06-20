import http.client, urllib.parse
import json

conn = http.client.HTTPSConnection('api.pushover.net')
conn.request('POST', '/1/messages.json', 
    urllib.parse.urlencode(
        {
            "token": "application_token", 
            "user": "user_token", 
            "message": "my message" # Update this to your desired message
        }
    ),
    {"Content-type": "application/x-www-form-urlencoded"}
)

response = conn.getresponse().read().decode()
response = json.loads(response)
if response["status"] == 1:
    print("Success: %s" % (response["request"]))
else:
    print("Error message didn't send see error: %s" % str(response))
