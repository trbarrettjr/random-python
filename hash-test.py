#!/usr/bin/env python3
import hashlib
import sys

def main():
    '''I want to fix this section to where you don't always have to have a filename to put in
    If you want to drop just the expected hashes like if you are going to curl something.'''
    if len(sys.argv) > 1: # If you want to give the file name, we can read it
        my_input = sys.argv[1]
        with open(my_input, 'rb') as f:
            my_input = f.read()
    else: # Read from the STDIN so that you can pipe a file in.
        my_input = sys.stdin.buffer.read()
      
    my_md5, my_sha1, my_sha256 = hash(my_input)
    print(f'MD5:\t{my_md5}\nSHA1:\t{my_sha1}\nSHA256:\t{my_sha256}')

    if '--md5' in sys.argv:
        desHash = sys.argv.index('--md5') + 1
        desHash = sys.argv[desHash]
        if my_md5 == desHash:
            print()
            print('MD5 Hashes Matches')
        else:
            warn = '* MD5 Hash does not match *'
            print()
            print('*' * len(warn))
            print(warn)
            print('*' * len(warn))
    elif '--sha1' in sys.argv:
        desHash = sys.argv.index('--sha1') + 1
        desHash = sys.argv[desHash]
        if my_sha1 == desHash:
            print()
            print('SHA1 Hashes Matches')
        else:
            warn = '* SHA1 Hash does not match *'
            print()
            print('*' * len(warn))
            print(warn)
            print('*' * len(warn))
    elif '--sha256' in sys.argv:
        desHash = sys.argv.index('--sha256') + 1
        desHash = sys.argv[desHash]
        if my_sha256 == desHash:
            print()
            print('SHA256 Hashes Matches')
        else:
            warn = '# SHA256 Hash does not match #'
            print()
            print('#' * len(warn))
            print(warn)
            print('#' * len(warn))

def hash(myData):
    a = hashlib.md5(myData).hexdigest()
    b = hashlib.sha1(myData).hexdigest()
    c = hashlib.sha256(myData).hexdigest()
    return a, b, c

if __name__ == '__main__':
    main()
