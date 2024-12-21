class Lesson:
    def __init__(self, title: str, teacher):
        """
        Initialize a Lesson instance.

        :param title: Title of the lesson.
        :param teacher: Teacher conducting the lesson.
        """
        self.title = title
        self.teacher = teacher

    def describe(self) -> str:
        """
        Describe the lesson.

        :return: A string description of the lesson.
        """
        return f"Lesson: {self.title}, conducted by {self.teacher.name}."