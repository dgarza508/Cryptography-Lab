# This one is purely for demonstration purposes
def gcd_from_notes(a: int, b: int) -> int:
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

#USE THIS ONE! (found online and much faster)
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)


def extended_gcd(a: int, b: int) -> int:
    
    #Returns (g, x, y) such that ax + by = g = gcd(a, b)
    
    if b == 0: 
        return (a, 1, 0)

    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)
