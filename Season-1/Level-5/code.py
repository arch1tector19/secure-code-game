# Welcome to Secure Code Game Season-1/Level-5!

# This is the last level of our first season, good luck!

import secrets
import os
import bcrypt

class Random_generator:

    # generates a random token
    def generate_token(self, length=8, alphabet=(
    '0123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )):
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    # generates salt
    def generate_salt(self, rounds=12):
        return bcrypt.gensalt(rounds)

class Bcrypt_hasher:

    def password_hash(self, password, salt):
        password = password.encode()
        if len(password) > 72:
            raise ValueError("Password exceeds bcrypt's 72-byte limit")
        return bcrypt.hashpw(password, salt).decode('ascii')

    def password_verification(self, password, password_hash):
        password = password.encode()
        if len(password) > 72:
            return False
        try:
            return bcrypt.checkpw(password, password_hash.encode('ascii'))
        except ValueError:
            return False

# Keep the old names for existing callers. Both use bcrypt.
SHA256_hasher = Bcrypt_hasher

class MD5_hasher(Bcrypt_hasher):
    def password_hash(self, password, salt=None):
        if salt is None:
            salt = bcrypt.gensalt()
        return super().password_hash(password, salt)

# a collection of sensitive secrets necessary for the software to operate
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
PASSWORD_HASHER = 'Bcrypt_hasher'


# Contribute new levels to the game in 3 simple steps!
# Read our Contribution Guideline at github.com/skills/secure-code-game/blob/main/CONTRIBUTING.md
