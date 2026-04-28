import pytest

from test_sample import func


@pytest.mark.parametrize(["input", "expected"], [(1, 2), (2, 3), (-1, 0), (1000, 1001)])
def test_increment(input, expected):
    result = func(input)
    assert result == expected


@pytest.mark.parametrize(
    ["input", "expected"], [("3+5", 8), ("7*9", 63), ("-11+3", -8)]
)
def test_evaluation(input, expected):
    result = eval(input)
    assert result == expected
