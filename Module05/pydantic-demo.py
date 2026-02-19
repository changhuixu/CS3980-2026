from datetime import datetime

from pydantic import BaseModel, PositiveInt, ValidationError


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {
    "id": 123,
    "Name": "Tom",  # notice this field is in uppercase 'N', and it will be ignored.
    "signup_ts": "2026-02-19 12:58",
    "tastes": {"wine": 9, "cabbage": "1"},
}


try:
    user = User(**external_data)

    print(user.id)
    print(
        user.name
    )  # you will see the default value for this field, because the "Name" is not assignable to "name"
    print(user.signup_ts)
    print(user.tastes)
except ValidationError as e:
    print(e.errors())
