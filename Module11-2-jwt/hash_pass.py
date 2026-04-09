import bcrypt


def hash_password(pwd: str):
    return bcrypt.hashpw()


def verify_password(input_pwd: str, db_pwd: str) -> bool:
    return bcrypt.checkpw(input_pwd, db_pwd)
