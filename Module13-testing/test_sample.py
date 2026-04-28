def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_answer_fail():
    result = func(3)
    assert result == 5, f"Expected 5 but got {result}"  # custom assertion error message
