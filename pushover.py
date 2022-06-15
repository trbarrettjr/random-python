import http.client, urllib.parse

conn = http.client.HTTPSConnection('api.pushover.net')
conn.request('POST', '/1/messages.json', 
    urllib.parse.urlencode(
        {
            "token": "application_token", 
            "user": "user_token", 
            "message": "Hello" # Update this to your desired message
        }
    ),
    {"Content-type": "application/x-www-form-urlencoded"}
)

print(conn.getresponse().read().decode())