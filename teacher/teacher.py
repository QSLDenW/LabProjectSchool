from person import Person

class Teacher(Person):
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject

    def introduce(self) -> str:
        return f"Hello, I am {self.name}, and I teach {self.subject}."