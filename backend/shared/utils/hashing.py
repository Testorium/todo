from typing import TypeAlias

from pwdlib import PasswordHash

password_hasher = PasswordHash.recommended()


HashedStr: TypeAlias = str


def hash_password(password: str) -> HashedStr:
    return password_hasher.hash(password)


def verify_password(password: str, hashed_password: HashedStr) -> bool:
    return password_hasher.verify(password=password, hash=hashed_password)
