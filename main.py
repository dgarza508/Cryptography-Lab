from modular_arithmetic import *
from dlp import bsgs, pohlig_hellman

# Options for tools
def tool_menu(): 
    print("\n=== Cryptography Toolkit ===")
    print("1. Modular arithmetic")
    print("2. Solve DLP (BSGS)")
    print("3. Solve DLP (Pohlig–Hellman)")
    print("0. Exit")

# Modular Arithmetic Options
def modular_menu():
    print("\n--- Modular Arithmetic ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exponentiation")
    print("5. Inverse")
    print("0. Back")

def run_modular():
    while True:
        modular_menu()
        choice = input("Choose: ")

        if (choice in {"0", "1", "2", "3", "4", "5"}):
            break
        else:
            print("Invalid choice. Please try again.\n")

    if (choice == "0"):
        return

    a = int(input("Enter a: "))
    b = int(input("Enter b (or exponent): "))
    m = int(input("Enter modulus m: "))

    if choice == "1":
        print(mod_add(a, b, m))
    elif choice == "2":
        print(mod_sub(a, b, m))
    elif choice == "3":
        print(mod_mul(a, b, m))
    elif choice == "4":
        print(mod_exp(a, b, m))
    elif choice == "5":
        print(mod_inv(a, m))


def main():
    while True:
        tool_menu()
        choice = input("Choose an option: ")

        if (choice == "1"):
            run_modular()
        elif (choice == "2"):
            p = int(input("p: "))
            g = int(input("g: "))
            h = int(input("h: "))
            print(bsgs(g, h, p))
        elif (choice == "3"):
            p = int(input("p: "))
            g = int(input("g: "))
            h = int(input("h: "))
            print(pohlig_hellman(g, h, p))
        elif (choice == "0"):
            break
        else:
            print("Invalid Choice")

# Apparently, it means only run if this is run directly
if (__name__ == "__main__"):
    main()


