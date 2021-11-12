#!/usr/bin/env python3
'''
A Basic function library that transposes the IPv4 addresses to Integers and Integers to IPv4 Addresses
Project Inspired by the Maxmind Database which stores IP addresses in the form of integers for faster processing.
'''
m1 = 256 ** 3
m2 = 256 ** 2
m3 = 256 ** 1
m4 = 256 ** 0

def ip_to_int(num_string):
    'Input String of IPv4 Address and get out an integer of the IP Address'
    if type(num_string) is str:
        o1, o2, o3, o4 = num_string.split('.')
    else:
        print('Number did not come in as string')
        exit()
    
    integer_ip = (int(o1) * m1) + (int(o2) * m2) + (int(o3) * m3) + (int(o4) * m4)

    return integer_ip

def int_to_ip(number):
    'Input an integer and outputs a string of the IPv4 Address'
    if type(number) is not int:
        number = int(number)
    elif type(number) is int:
        pass
    else:
        print('Number cannot be returned as an integer')
        exit()

    o1 = (int(number) / m1) % 256
    o2 = (int(number) / m2) % 256
    o3 = (int(number) / m3) % 256
    o4 = (int(number) / m4) % 256

    return '{}.{}.{}.{}'.format(int(o1), int(o2), int(o3), int(o4))