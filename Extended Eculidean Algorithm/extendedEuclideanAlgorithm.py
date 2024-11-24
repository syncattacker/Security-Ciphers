#!/usr/bin/env python

import os
from art import text2art

def banner() -> None:
    '''
    Prints the banner for the Extended Euclidean Algorithm for finding Modular Inverse.
    '''
    print(text2art('\nextended euclideam algorithm', font = "usa_flag"))
    print("Developed and maintained by : @syncattacker")


def calculateInverse(key : int, domain : int) -> int:
    '''
    Calculates the Modular Inverse of the Key with respect to the domain.
    '''
    copyDomain = domain
    t1, t2 = 0, 1
    while key > 0:
        quotient = domain // key
        remainder = domain % key
        domain, key = key, remainder
        t1, t2 = t2, t1 - quotient * t2

    if domain != 1:
        return -1

    return t1 % copyDomain



print(calculateInverse(5, 26))