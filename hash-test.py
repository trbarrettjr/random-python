#!/usr/bin/env python3
import sys
import hashlib

args = sys.argv[1:]

if len(args) >= 2:
    the_file = args[0]
    known = args[1]

# print(sys.argv)

f = open(the_file, 'rb')
contents = f.read()
the_hash = hashlib.sha256(contents).hexdigest()

# contents = sys.stdin.buffer.read()

print("MD5:\t", hashlib.md5(contents).hexdigest())
print("SHA1:\t", hashlib.sha1(contents).hexdigest())
print("SHA256:\t", hashlib.sha256(contents).hexdigest())

if the_hash in known:
    print("The hash matches!")