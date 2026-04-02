import os

name = os.getenv("MY_NAME")
print(f"Hello {name}, from Python")

value = os.getenv("MY_VALUE", 42)
print(f"Value is {value}")  # cannot parse it as an integer

is_prod = os.getenv("IS_PROD", True)
if is_prod:
    print(f"Prod: {is_prod}")
else:
    print("not prod")
