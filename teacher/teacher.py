
class Teacher :
    def __init__(self, name: str, subject: str):
        """
        Initialize a Teacher instance.

        :param name: Name of a teacher.
        :param subject: Subject teacher specialised in.
        """

        self.name= name
        self.subject = subject

    def introduce(self) -> str:
        """
        Introduce the teacher.

        :return: str introducing the teacher.
        """

        return f"Hello, I am {self.name}, and i teach {self.subject}."

