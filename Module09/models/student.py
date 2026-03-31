from beanie import Document


class Student(Document):
    univ_id: str
    name: str
