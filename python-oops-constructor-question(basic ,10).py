#✅ 1. Create a class with a constructor and print student details
class Student():
    def __init__(self,name,roll_no,enroll_no,course,passing_year):
        self.name = name
        self.roll_no = roll_no
        self.enroll_no = enroll_no
        self.course = course
        self.passing_year = passing_year

    def __str__(self):
         return f"{self.name} ({self.roll_no}) ---> {self.course}"

    def display(self):
        print(f"your name is {self.name}\nyou are the student of {self.course}")
    def passing_status(self):
        print(f"your will be pass in the year{self.passing_year}")


student_1 = Student("parul pal",28,456789,"btech(cse)",2026)
print(student_1.name)
print(student_1.roll_no)
student_1.display()
student_1.passing_status()
print(student_1)


