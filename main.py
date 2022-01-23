import hashlib
import hmac
import random
import string

# Generate a "Provably Fair" number between 1 and n

SERVER_SEED_LENGTH = 64


def generate(client_seed: str, nonce: int, max_number: int = 10000):
    client_seed = ''.join(  # Random 16 character server seed with only lowercase and digits
        random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(16)) if client_seed is None else client_seed
    server_seed = ''.join(  # Random 64 character server seed with only lowercase and digits
        random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(SERVER_SEED_LENGTH))
    print("Server Seed Hash:", hashlib.sha256(server_seed.encode("utf-8")).hexdigest())
    key = "%s:%s:%s" % (nonce, server_seed, nonce)  # HMAC Secret Key
    client = "%s:%s:%s" % (nonce, client_seed, nonce)  # HMAC Client Key
    signature = hmac.new(
        key.encode("utf-8"),
        client.encode("utf-8"),
        hashlib.sha512).hexdigest()  # HMAC-SHA512 Hash
    decimal = int(signature[:8], 16)  # Convert first 8 characters to base 16 decimal
    return min(round(decimal / (42.94967295 * max_number)), max_number)  # To whole number and ensure number <= max_number


if __name__ == "__main__":
    print("Generated Number:", generate(str(input("Client Seed: ")), 0))
