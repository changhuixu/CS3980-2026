# conftest.py is a special pytest file
# — fixtures defined in it are automatically available
# to all test files in that directory and its subdirectories.

import pytest


@pytest.fixture(scope="session")
def stage_user():
    return {"id": 1, "name": "Alice", "age": 22}
