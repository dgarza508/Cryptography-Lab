from utils import gcd, extended_gcd

# This file is mostly for demonstration purposes

def mod_add(a, b, m):
    return (a + b) % m


def mod_sub(a, b, m):
    return (a - b) % m


def mod_mul(a, b, m):
    return (a * b) % m


def mod_exp(base, exp, mod):
    # Do NOT use next two! This is purely for demonstration.
    # We will use pow from import math for efficiency

    
    result = 1
    base %= mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2

    return result

def mod_inv(a, m):
    """
    Modular inverse using Extended Euclidean Algorithm
    (demonstration)
    """
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m
