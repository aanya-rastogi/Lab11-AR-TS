import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    try:
        return math.log(b,a)
    except ValueError:
        raise ValueError

def exponent(a,b):
    return a**b




def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError

    return b / a

def log(a, b):
    if b <= 0:
        raise ValueError
    if a == 1:
        raise ValueError
    if a <= 0:
        raise ValueError

    return math.log(b, a)

def exp(a, b):
    return a ** b
