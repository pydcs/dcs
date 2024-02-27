"""
The password module generates DCS compliant passwords from input string
"""

import hashlib
import base64
import string
import random


def password_hash(password: str) -> str:
    # see https://www.reddit.com/r/hoggit/comments/uf2sh0/psa_creating_the_new_slot_passwords_outside_of_dcs/

    # encode from https://github.com/simonwhitaker/base64url
    def encode(b: bytes, trim: bool = False, break_at: int = 0) -> str:
        encoded_string = base64.urlsafe_b64encode(b).decode("utf-8")
        if trim:
            encoded_string = encoded_string.rstrip("=")

        if break_at > 0:
            i = 0
            result = ""
            while i < len(encoded_string):
                result += encoded_string[i: i + break_at] + "\n"
                i += break_at
            return result
        else:
            return encoded_string

    SALT_SIZE = 11
    DIGEST_SIZE = 32

    key = ''.join(random.sample(string.digits + string.ascii_letters, SALT_SIZE))
    p_hash = hashlib.blake2b(key=key.encode(), digest_size=DIGEST_SIZE)
    p_hash.update(password.encode())
    b64url_hash = encode(p_hash.digest(), trim=True)

    return key + ":" + b64url_hash
