import random


def generate_private_key(p: int) -> int:
    if p <= 3:
        raise ValueError("p must be > 3")
    return random.randint(2, p - 2)
 


def generate_public_key(g: int, private_key: int, p: int) -> int:
    
    # Compute public key
    
    return pow(g, private_key, p)


def shared_secret(private_key: int, other_public: int, p: int) -> int:
    
    # Compute shared secret
    
    return pow(other_public, private_key, p)


def verify(shared_secret_alice: int, shared_secret_bob: int) -> bool:
    
    # Check both sides derived the same secret.
    
    return shared_secret_alice == shared_secret_bob


def demo_diffie_hellman(p: int, g: int) -> None:

    print("    Diffie–Hellman Demo    ")
    print(f"Public parameters:\n  p = {p}\n  g = {g}\n")

    # Alice generates keys
    alice_private = generate_private_key(p)
    alice_public = generate_public_key(g, alice_private, p)

    # Bob generates keys
    bob_private = generate_private_key(p)
    bob_public = generate_public_key(g, bob_private, p)

    print("Alice keys:")
    print(f"  private a = {alice_private}")
    print(f"  public  A = g^a mod p = {alice_public}\n")

    print("Bob keys:")
    print(f"  private b = {bob_private}")
    print(f"  public  B = g^b mod p = {bob_public}\n")

    # Each computes the shared secret
    alice_secret = shared_secret(alice_private, bob_public, p)
    bob_secret = shared_secret(bob_private, alice_public, p)

    print("Shared secrets computed:")
    print(f"  Alice computes s = B^a mod p = {alice_secret}")
    print(f"  Bob computes   s = A^b mod p = {bob_secret}\n")

    ok = verify(alice_secret, bob_secret)
    if (ok):
        print("Verification Successful!")
    else:
        print("Verification Failed!")


if __name__ == "__main__":
    # For a simple demo, you can use a small prime.
    # This is NOT secure for real cryptography—just for learning.

    p = 23 # Placeholder for user input 
    g = 5 # Placeholder for user input

    """
    The following two lines are for user inputs. 
    We still need prime checks and generator verifying for full functionality
    Do not uncomment unless you have fully implemented those functions
    """
    # p = int(input("Enter prime p: "))
    # g = int(input("Enter generator g: "))

    demo_diffie_hellman(p, g)
