import bcrypt


def hash_password(pwd: str) -> bytes:
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())


def verify_password(input_pwd: str, db_pwd: str) -> bool:
    return bcrypt.checkpw(input_pwd.encode(), db_pwd.encode())


# a = hash_password("hi124")
# print(a)

# a = hash_password("hi124Super")
# print(a)
