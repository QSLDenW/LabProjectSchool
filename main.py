
def main():
    from teacher.teacher import Teacher
    from student.student import Student
    from room.room import Room


    teacher = Teacher("Maksym Kaplun", "JavaScript")

    student1 = Student("Denys", 14)
    student2 = Student("Matvii", 14)

    room = Room("C2112")
    room.assing_teacher(teacher)
    room.add_students(student1, student2)

    print(room.describe())


if __name__ == "__main__":
    main()

