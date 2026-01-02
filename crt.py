from utils import gcd, extended_gcd


def crt_two(a1, m1, a2, m2):

    """
    Solve:
        x ≡ a1 (mod m1)
        x ≡ a2 (mod m2)
    Assumes gcd(m1, m2) = 1
    """

    if (gcd(m1, m2) != 1):
        return None

    _, s, t = extended_gcd(m1, m2)
    return (a1 * t * m2 + a2 * s * m1) % (m1 * m2)


def crt_many(congruences):

    
    #congruences = [(a1, m1), (a2, m2), ...]
    

    x, m = congruences[0]

    for a_i, m_i in congruences[1:]:
        x = crt_two(x, m, a_i, m_i)
        m *= m_i

    return x
