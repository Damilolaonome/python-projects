
import hashlib
import secrets
import hmac


def hash_password(password):
    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600_000
    )

    return salt, password_hash


def verify_password(password, salt, stored_hash):
    candidate_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600_000
    )

    return hmac.compare_digest(candidate_hash, stored_hash)


# Use a password created specifically for this lab.
test_password = "Onome.umukoro2"

salt, stored_hash = hash_password(test_password)

print("Password hash created successfully.")
print("Salt:", salt.hex())
print("Stored hash:", stored_hash.hex())

guess = input("\nEnter a password to verify: ")

if verify_password(guess, salt, stored_hash):
    print("Password verified successfully.")
else:
    print("Password does not match.")




