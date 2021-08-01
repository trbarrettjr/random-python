#!/usr/bin/env python3

def evaluate(number):
    if number % 2 == 0:
        return even(number)
    else:
        return odd(number)

def odd(number):
    return 3 * number + 1

def even(number):
    return number // 2