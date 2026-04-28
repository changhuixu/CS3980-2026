import pytest

TOLERANCE = pow(10, -6)


def test_float_numbers():
    result = 0.1 + 0.2
    error = result - 0.3
    assert error < TOLERANCE
    assert result == pytest.approx(0.3)
