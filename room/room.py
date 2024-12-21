class Room:
    def __init__(self, name: str):
        self.name = name
        self.teacher = None
        self.students = []
        self.janitor = None
        self.lessons = []

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def add_students(self, *students):
        self.students.extend(students)

    def assign_janitor(self, janitor):
        self.janitor = janitor

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def describe(self) -> str:
        description = f"Room {self.name} contains:\n"

        if self.teacher:
            description += f"  Teacher: {self.teacher.name} (teaches {self.teacher.subject})\n"
        else:
            description += "  No teacher assigned.\n"

        if self.students:
            description += "  Students:\n"
            for student in self.students:
                description += f"    - {student.name}, {student.age} years old\n"
        else:
            description += "  No students in the room.\n"

        if self.janitor:
            description += f"  Janitor: {self.janitor.name}\n"
        else:
            description += "  No janitor assigned.\n"

        if self.lessons:
            description += "  Lessons:\n"
            for lesson in self.lessons:
                description += f"    - {lesson.describe()}\n"
        else:
            description += "  No lessons scheduled.\n"

        return description
