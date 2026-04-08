import bcrypt


def hash_password(password: str) -> bytes:
    password_bytes = password.encode()
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed


def verify_password(input_password: str, db_password: str) -> bool:
    return bcrypt.checkpw(input_password.encode(), db_password)


my_pass = "super_secret999####**"
my_db_hashed_pass = hash_password(my_pass)

print(my_db_hashed_pass)
print(verify_password(my_pass, my_db_hashed_pass))

my_wrong_pass = "super_secret999###**"
print(verify_password(my_wrong_pass, my_db_hashed_pass))


a = bcrypt.gensalt()
print(a)
print(a[-1])
print(chr(a[-1]))

b = bcrypt.gensalt()
print(b)
print(b[-1])
print(chr(b[-1]))
