"""
Test file on xor a file to obfuscate a file.

Don't use!  Not Secure
"""
#!/usr/bin/python3
import sys

for filename in sys.argv[1:]:
  print("Encrypting", filename)
  new_file = filename.replace('.txt', '.enc')
  b = bytearray(open(filename, "rb").read())
  for i in range(len(b)):
    b[i] ^= 0b100100 # I randomly utilize generated this random bit.  NOT SECURE
  open(new_file, "wb").write(b)
