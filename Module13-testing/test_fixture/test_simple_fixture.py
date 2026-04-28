import pytest


def test_user_name(stage_user):
    result = stage_user["name"]
    assert result == "Alice"


def test_user_age(stage_user):
    assert stage_user["age"] > 18
