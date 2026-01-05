import math
from utils import gcd
from crt import crt_many

# Baby Step Giant Step Algorithm
def bsgs(g: int, h: int, p: int) -> int:
    
    # Solve g^x ≡ h (mod p)
    
    n = math.isqrt(p - 1) + 1

    # Baby steps
    baby = {}
    cur = 1
    for a in range(n):
        if (cur not in baby):
            baby[cur] = a
        cur = (cur * g) % p

    g_inv = pow(g, -1, p)
    factor = pow(g_inv, n, p)

    # Giant steps
    cur = h
    for b in range(n):
        if (cur in baby):
            return baby[cur] + b * n
        cur = (cur * factor) % p

    return None

# Calls bsgs for the purpose of Pohlig-Hellman
def bsgs_prime_power(g: int, h: int, p: int, q: int, e: int) -> int:
    
    # Solve g^x = h mod p where order divides q^e

    x = 0
    g_inv = pow(g, -1, p)

    for k in range(e):
        g_k = pow(g, q ** (e - 1 - k), p)
        h_k = pow((h * pow(g_inv, x, p)) % p, q ** (e - 1 - k), p)

        d = bsgs(g_k, h_k, p)
        x += d * (q ** k)

    return x


def pohlig_hellman(g: int, h: int, p: int) -> int:

    # Solve g^x ≡ h (mod p) using Pohlig–Hellman    

    n = p - 1
    factors = {}

    # Factor n
    d = 2
    while (d * d <= n):
        while (n % d == 0):
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if (n > 1):
        factors[n] = 1

    congruences = []

    for q, e in factors.items():
        g_i = pow(g, (p - 1) // (q ** e), p)
        h_i = pow(h, (p - 1) // (q ** e), p)

        x_i = bsgs_prime_power(g_i, h_i, p, q, e)
        congruences.append((x_i, q ** e))

    return crt_many(congruences)

