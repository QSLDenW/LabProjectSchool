from person import Person

class Student(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age

    def introduce(self) -> str:
        return f"Hello, I am {self.name}, and I'm {self.age} years old."