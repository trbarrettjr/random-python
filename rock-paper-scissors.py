#!/usr/bin/python3
import random
import sys
import time

choices = ["rock", "paper", "scissors"]

def main():
    choice = random.choice(choices)
    return choice

if __name__ == "__main__":
    i = 0
    options = list()
    while i < 100000:
        value = main()
        options.append(value)
        i += 1

    for i, v in enumerate(options):
        options[i] = v + '\n'

    with open('rps.txt', 'w') as f:
        f.writelines(options)
