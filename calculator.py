# https://github.com/aanya-rastogi/Lab11-AR-TS
# Partner 1: Aanya Rastogi
# Partner 2: Tobin Swiger

import math
"""
calculator.py
- Defines functions used to create a simple calculator
"""

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError

    return b / a

def logarithm(a, b):
    try:
        return math.log(b,a)
    except ValueError:
        raise ValueError

def exp(a, b):
    return a ** b

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError

def hypotenuse(a,b):
    return math.hypot(a, b)
