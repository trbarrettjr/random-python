# random-python

Random Python Applications that I have done.

---

# Obfuscation Themed Python

## enc.py

This is a simple xor script.  I was testing it for something, but decided not going to work with it.
**This is not secure for encryption!  DO NOT USE!!!**

### text.text
Orignal text file that was used to XOR

### text.enc
Encoded file from the text file after being XOR'd (if that is a word!)

## onetimepad

Reading from Bruce Schnier's book and was talking about one time pads.  I tried my hand at making a one-time pad via python.  Meh...
**This is probably not secure for encryption! DO NOT USE!!**. I know it is from Bruce Schnier, but...

---

# Hash Themed Python
## hash-test.py
This file was testing to see if a file can be hashed and have the hash compared to the known hash.  The idea came from downloading software from the internet and unable to adequately compare the SHA256 hash to the known hash from the vendor.

`cat [filename] | ./hash-test` or  
`./hash-test.py < [file]` or  
`./hash-test.py [filename] --sha256 [sha256 string]` or  
`./hash-test.py [filename] --sha1 [sha1 string]` or   
`./hash-test.py [filename] --md5 [md5 string]`

### To-do
I would like to work the algorithm a little bit where you can pipe something in and give the known hash so that it compares.  For example:
`curl [file from web] | ./hash-test.py --sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709`

Currently have an if statement in there where `if sys.argv > 1` then it would assume there is a filename there.  Thinking of conditional where `if sys.argv == 3` then it will assume a pipe is going to happen.  Work in progress.

---

# Math Themed Python

These files are math problems that I try to solve or play with.  Nothing really to exciting.

## declination.py

Working on the sun declination calculator.  This is to calculate the sun's location relative to the earth.  Will need to add more code to calculate the declination relative to latitude.

## euclid.py

I was helping my daughter with her math homework and was having trouble with reducing fractions.  I went through her homework and did my best to explain how euclid's algoritm worked and then wrote this little program to help display how to find the **greatest common factor**.

## collatz.py

This is of [The Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture).  This is just a quick library that I programmed up and use the IDE to test some random number.  I don't think that I am going to solve the *Collatz Conjecture* with this program but it is nice to play with.

To use, I wrote the little program in the IDE.

```python3
import collatz

num = int(7) # Can be any positive integer.
found = [] # Make an empty list

while num > 1: # Do this or your sequence will forever be in a 4, 2, 1 loop!
    found.append(num)
    num = collatz.evaluate(num)
```

You can then type in the variable `found` in the IDE to get the list of the collatz conjecture!  **Not Solved** — Ask your local university mathmatician!

## ipfunc.py

This is inspired by the MaxMind Database.  The database stores IPv4 addresses as integers for easy lookup and sorting.  I wrote this to tranpose IPv4 address numbers to integers and integers to IPv4 addresses.

To use
```python3
import ipfunc

# These functions will try to correct themselves to the proper input (str or int), however, they can return an error.

a = ipfunc.ip_to_int('127.0.0.1') # Please note that the input to the function is a str
b = ipfunc.int_to_ip(2130706433) # Please note that the input to the function is an int
```

---

# Internet Python

## google-domains.py

This is a little home-brew application that you are able to update your Google Domains DynDNS through their [API](https://support.google.com/domains/answer/6147083?hl=en#zippy=%2Cuse-the-api-to-update-your-dynamic-dns-record).

To utilize update lines 5 and 6 with the Username, Password, and domain and the program will do the rest.

```python3
credentials = (b'username', b'password') # Place username and Password from Google Domains
hostname = b'sub.domain.tld' # Place domain name here from your google domains DynDNS
```

**Warning**: Please note that saving credentials in the application is not secure; please utilize some safe method to securely store and recall you credentials as needed.

**SAD** 😢 Google decided to shutdown its domain business.  So do with this what you will.

## pushover.py

This will reach out and send a message using [pushover.net](https://www.pushover.net) service.  This can be modified to allow for each purpose and even made into a class function.

**Warning**: Please note that saving credentials in the application is not secure, please utilize some safe method to securely store and recall your credentials as needed.

## tailscale-api.py

Playing with [Tailscale VPN](https://tailscale.com/) service.  They have an [API](https://github.com/tailscale/tailscale/blob/main/api.md) that you are able to utilize.  This is just calling the API and getting all the devices that are authorized for my account.  Adjust as you see fit.

**Warning**: Please note that saving credentials in the application is not secure, please utilize some safe method to securely store and recall your credentials as needed.

## ts-exit.py

While using [Tailscale's](https://tailscale.com) [exit nodes](https://tailscale.com/kb/1103/exit-nodes), I like to enable and disable the dns settings while enabling and disabling the exit nodes.

So this is a Python script of it taking in the information and connecting and disconnecting to how I like it.  I may update this into the future to including doing and ip check on a website that will return your ip address before and after connection.
