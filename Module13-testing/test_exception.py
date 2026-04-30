import pytest


def f():
    print("I am here")
    raise SystemExit(1)


def test_m():
    with pytest.raises(SystemExit):
        f()
        # print("I am done")
