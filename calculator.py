import math

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b/a


def logarithm(a, b):
    try:
        return math.log(b,a)
    except ValueError:
        raise ValueError

def exponent(a,b):
    return a**b





