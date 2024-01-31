class School:

    all=[]
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been added to {self.name}.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student.name} has been removed from {self.name}.")
        else:
            print(f"{student.name} is not a student at {self.name}.")

    def list_students(self):
        if not self.students:
            print(f"There are no students at {self.name}.")
        else:
            print(f"Students at {self.name}:")
            for student in self.students:
                print(f"- {student.name}")

class Student:
    all = []


    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.text_file = f"{name}_welcome.txt"
        Student.all.append(self)

    def write_to_file(self, content):
        with open(self.text_file, 'w') as file:
            file.write(content)

            print(f"Message has been written to {self.name}'s file.")

    def __repr__(self):
            return f"{self.name} {self.age } { self.grade} "

# דוגמאות שימוש:
# יצירת ישוב חדש
my_school = School(name="My School", location="Cityville")

# יצירת תלמידים
student1 = Student(name="Alice", age=15, grade=10)
student2 = Student(name="Bob", age=16, grade=11)

# הוספת תלמידים לבית ספר
my_school.add_student(student1)
my_school.add_student(student2)

# הצגת רשימת התלמידים בבית הספר
my_school.list_students()

# הסרת תלמיד מבית הספר
# my_school.remove_student(student1)
# print (my_school.students)
# # עדכון רשימת התלמידים
# my_school.list_students()
# student1.write_to_file("חיחעח")
# student1.text_file
print(Student.all)

