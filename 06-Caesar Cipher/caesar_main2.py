class ShiftCipher:
    """Class for doing encryption and decryption using a Shift cipher."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""

        encoder = [None] * 26  # temp list for encryption
        decoder = [None] * 26  # temp list for decryption

        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))

        self._forward = ''.join(encoder)  # will store as string
        self._backward = ''.join(decoder)  # since fixed

    def encrypt(self, message):
        """Return string representing encripted message."""

        return self.transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""

        return self.transform(secret, self._backward)

    def transform(self, original, code):
        """Utility to perform transformation based on given code string."""

        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index from 0 to 25
                msg[k] = code[j]  # replace this character
            elif msg[k].islower():
                j = ord(msg[k]) - ord('a')  # index from 0 to 25
                msg[k] = chr(ord(code[j]) + 32)  # replace this character with the respective lower case since,
                                                 # the code is in uppercase
            else:  # to handle symbols and other character like space
                msg[k] = original[k]
        return ''.join(msg)


def attack(msg):
    """Function to determine the code using brute force"""

    for key in range(26):
        c = ShiftCipher(key)
        print(c.decrypt(msg), "-", key)

"""Driver Program"""

message = 'Introduction-TO$CRYPTOGRAPHIC TECHNIQUES'
k = 3

print("")

caesar = ShiftCipher(3)
coded = caesar.encrypt(message)
print("Caesar Cipher:", coded)
answer = caesar.decrypt(coded)
print("Message:", answer)

print("")

shift = ShiftCipher(k)
coded = shift.encrypt(message)
print("Shift Cipher", k, ":", coded)
answer = shift.decrypt("QHWZRUNLQJ SRVVLELOLWLHV")
print("Message:", answer)

print("")

attack(coded)
