import random
from math import gcd

def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_prime(start, end):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_key_pair(keysize=1024):
    p = generate_prime(2**(keysize // 2 - 1), 2**(keysize // 2))
    q = generate_prime(2**(keysize // 2 - 1), 2**(keysize // 2))
    while q == p:
        q = generate_prime(2**(keysize // 2 - 1), 2**(keysize // 2))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = modular_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    try:
        message = [ord(char) for char in plaintext]
        cipher = [pow(m, e, n) for m in message]
        return cipher
    except Exception as error:
        raise ValueError(f"Encryption failed: {error}")

def decrypt(private_key, ciphertext):
    d, n = private_key
    try:
        decrypted_message = [chr(pow(c, d, n)) for c in ciphertext]
        return ''.join(decrypted_message)
    except Exception as error:
        raise ValueError(f"Decryption failed: {error}")

def main():
    print("Generating RSA key pair...")
    public_key, private_key = generate_key_pair(16) 
    print(f"Public Key: {public_key}\nPrivate Key: {private_key}")

    message = "My Name is Prabhat"
    print(f"Original Message: {message}")

    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
