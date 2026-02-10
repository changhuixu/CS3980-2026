from typing import Annotated


def say_hello(name: Annotated[str, "show me some more info"]) -> str:

    return f"Hello {name}"


say_hello("Adam")
