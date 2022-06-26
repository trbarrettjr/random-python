import http.client
from urllib.parse import urlencode
import base64

credentials = (b'username', b'password') # Place username and Password from Google Domains
hostname = b'sub.domain.tld' # Place domain name here from your google domains DynDNS
encoded = base64.b64encode(credentials[0] + b':' + credentials[1]).decode()

def main(): #This function will automattically fill-in the values and work for you!
    message = urlencode(
        {'hostname': hostname,}
    )
    headers = {"Content-Type": "application/x-www-form-urlencoded", 
        "User-agent": "DynDNS for Google API/1.0.0 email@domain.tld", # Be Cool and put your email address in there in case somebody needs to contact you.
        'Authorization': 'Basic %s' % encoded}
    conn = http.client.HTTPSConnection('domains.google.com') # Google Domains 
    conn.request('POST', '/nic/update', message, headers) # Watch API documentation for the change

    google_response = conn.getresponse().read().decode() # Decode the binary string, and file-like object
    if 'good' in google_response or 'nochg' in google_response: # Tests if good response from Google
        print('Update Successful:', google_response)
    else: # If you have a bad return, this will notify you!
        print('*' * (len(google_response) + 4))
        print('* ' + google_response + ' *')
        print('*' * (len(google_response) + 4))

if __name__ == '__main__':
    main()
