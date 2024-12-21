from person import Person

class Janitor(Person):
    def __init__(self, name: str):
        super().__init__(name)

    def introduce(self) -> str:
        return f"Hello, I am {self.name}, the janitor. I keep the rooms clean."