#!/usr/bin/env python3
from math import *

def euclid_algo(x, y, verbose=True):
    if x < y: # we want x >= y
        return euclid_algo(y, x, verbose)
    print()
    while y != 0:
        if verbose:
            print('%s = %s * %s + %s' % (x, floor(x/y), y, x % y))
        (x, y) = (y, x % y)
    
    if verbose: print('Greatest common factor is: %s' % x)
    return x