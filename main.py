import hashlib
import hmac
import random
import string

# Generate a "Provably Fair" number between 1 and 10000

CLIENT_SEED = "cmY7dvn29lV7WcEi"  # Client editable seed
SERVER_SEED_LENGTH = 64
SPECIAL_NUMBER = 429496.7295


def generate(nonce: int):
    serverSeed = ''.join(  # Random 64 character server seed with only lowercase and digits
        random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(SERVER_SEED_LENGTH))
    print(hashlib.sha256(serverSeed.encode("utf-8")))
    key = "%s:%s:%s" % (nonce, serverSeed, nonce)  # HMAC Secret Key
    client = "%s:%s:%s" % (nonce, CLIENT_SEED, nonce)  # HMAC Client Key
    signature = hmac.new(
        key.encode("utf-8"),
        client.encode("utf-8"),
        hashlib.sha512).hexdigest()  # HMAC-SHA512 Hash
    decimal = int(signature[:8], 16)  # Convert first 8 characters to base 16 decimal
    return min(round(decimal / SPECIAL_NUMBER), 10000)  # To whole number and ensure number <= 10000


def main():
    for nonce in range(1, 2):
        print(generate(nonce))


if __name__ == "__main__":
    main()
