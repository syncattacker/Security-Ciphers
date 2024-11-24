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
    inverse = 0
    if key != 0: 
        quotient = domain // key
        remainder = domain % key
        t1 = 0
        t2 = 1
        t3 = t1 - (quotient * t2)
        while remainder > 0:
            domain = key
            key = remainder
            quotient = domain // key
            remainder = domain % key
            t1 = t2
            t2 = t3
            t3 = t1 - (quotient * t2)
            inverse = t2
    return inverse



