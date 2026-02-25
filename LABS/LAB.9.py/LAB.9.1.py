class Person:
    """Base class representing a person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


class Student(Person):
    """Student class inheriting from Person"""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"Hi, I'm {self.name}, a student. My ID is {self.student_id} and I'm {self.age} years old."


class Teacher(Person):
    """Teacher class inheriting from Person"""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"Hello, I'm {self.name}, a teacher. I teach {self.subject} and I'm {self.age} years old."


# Testing the classes

student1 = Student("Cagla", 16, "S101")
student2 = Student("Alyssa", 17, "S102")

teacher1 = Teacher("Max", 40, "Physics")
teacher2 = Teacher("Daniel", 35, "Mathematics")   # ← Yeni eklenen teacher

print("=== School Management System ===")

print(student1.introduce())
print(student2.introduce())

print(teacher1.introduce())
print(teacher2.introduce())   # ← Yeni teacher output

print("\nTeacher 1 subject:", teacher1.subject)
print("Teacher 2 subject:", teacher2.subject)