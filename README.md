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

`./hashtest.py [filename] [sha256 string]`

---

# Math Themed Python

These files are math problems that I try to solve or play with.  Nothing really to exciting.

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
