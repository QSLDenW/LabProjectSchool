def main():
    from teacher.teacher import Teacher
    from student.student import Student
    from room.room import Room
    from janitor.janitor import Janitor
    from lesson.lesson import Lesson

    teacher = Teacher("Maksym Kaplun", "JavaScript")

    student1 = Student("Denys", 14)
    student2 = Student("Matvii", 14)

    room = Room("C2112")

    janitor = Janitor("Ivan Ivanov")
    lesson = Lesson("JavaScript Basics", teacher)

    room.assign_teacher(teacher)
    room.add_students(student1, student2)
    room.assign_janitor(janitor)
    room.add_lesson(lesson)

    print(room.describe())


if __name__ == "__main__":
    main()