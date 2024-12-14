
class Room:
    def __init__(self, name: str):
        """
        Initialize a room instance.

        :param name: Name of a classroom.
        """

        self.name= name
        self.teacher = None
        self.students = []

    def assing_teacher(self, teacher):
        self.teacher = teacher

    def add_students(self, *students):
        self.students.extend(students)

    def describe(self) -> str: 
        """ 
        Describe the room, listing the teacher and students. 
 
        :return: A string description of the room. 
        """ 
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
 
        return description


