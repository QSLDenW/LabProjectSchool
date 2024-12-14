
class Student :
    def __init__(self, name: str, age: int):
        """
        Initialize a Student instance.

        :param name: Name of a student.
        :param age: Student's age.
        """

        self.name= name
        self.age = age

def introduce(self) -> str:
        """
        Introduce the student.

        :return: str introducing the student.
        """

        return f"Hello, I am {self.name}, and i'm {self.age} years old."

