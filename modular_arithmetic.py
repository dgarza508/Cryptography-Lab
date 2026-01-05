from utils import gcd, extended_gcd

# This file is mostly for demonstration purposes

def mod_add(a: int, b: int, m: int) -> int:
    return (a + b) % m


def mod_sub(a: int, b: int, m: int) -> int:
    return (a - b) % m


def mod_mul(a: int, b: int, m: int) -> int:
    return (a * b) % m


def mod_exp(base: int, exp: int, mod: int):

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

def mod_inv(a: int, mod: int) -> int:
    
    # Do NOT use next two! This is purely for demonstration.
    # For future, we will check gcd == 1, then 
    # We will use pow from import math for efficiency
    
    g, x, _ = extended_gcd(a, mod)
    if g != 1:
        return None
    return x % mod
