dict = {"brand": "Ford", "year": 1967, "year": 1999}

print(dict)


def my_sum(*args):
    result = 0
    for x in args:
        result += x

    return result


a = my_sum(1, 2, 3, 4, 5, 6)
print(a)
