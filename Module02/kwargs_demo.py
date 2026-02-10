def concatenate(**kwargs):
    """
    Docstring for concatenate

    :param kwargs: Description
    """
    result = ""
    user = kwargs["username"]
    print("username =", user)
    for a in kwargs.values():
        
        if type(a) is str:
            result += a

    return result


temp_string = concatenate(brand="her", username="Hi", year=6)
print(temp_string)

help(concatenate)
