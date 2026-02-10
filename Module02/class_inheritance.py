class Person:
    def __init__(self, fname: str, lname: str):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)


p1 = Person("Henry", "Hi")
p1.print_name()


class Student(Person):
    def __init__(self, fname: str, lname: str, year: int):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduation_year,
        )


x = Student("Mike", "Olsen", 2025)
x.welcome()
