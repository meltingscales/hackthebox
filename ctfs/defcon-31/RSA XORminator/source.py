from Crypto.Util.number import GCD, getPrime, inverse, bytes_to_long, long_to_bytes

from secret import FLAG


class RSA:

    def __init__(self, key_length):
        self.e = getPrime(1024)

        while True:
            p, q = getPrime(key_length // 2), getPrime(key_length // 2)
            phi = (p-1)*(q-1)
            self.n = p * q
            if GCD(self.e, phi) == 1 and self.e < self.n:
                break

        self.d = inverse(self.e, phi)

    def encrypt(self, message):
        message = bytes_to_long(message)
        return long_to_bytes((message ^ self.e) % self.n)

    def decrypt(self, encrypted_message):
        message = (encrypted_message ^ self.d) % self.n
        return long_to_bytes(message)


def main():
    rsa = RSA(1024)
    ciphertext = rsa.encrypt(FLAG)

    with open("output.txt", "w") as f:
        f.write(f"{rsa.n}\n{rsa.e}\n{ciphertext.hex()}")


if __name__ == "__main__":
    main()
