
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

#✅ 2. Constructor to calculate area & perimeter of triangle
class Triangle():
    def __init__(self,side_1,side_2,side_3,height,base):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.height = height
        self.base = base

    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

triangle_1 = Triangle(5,5,8,3,8)
print("the area of the triangle:",triangle_1.area())
print("the perimeter of the triangle :",triangle_1.perimeter

#✅ 3. Constructor in class to find the square of a number
class power():
    def __init__(self,num):
        self.num = num

    def square(self):
        return self.num ** 2
    def cube(self):# additional
        return self.num ** 3
num_1 = power(4)
print(f"square of  {num_1.num}:", num_1.square())
print(f"cube of {num_1.num}",num_1.cube())

#✅ 4. Constructor to store and print employee data
class Employee():
    def __init__(self,name,contact_no,address):
        self.name = name
        self.contact_no = contact_no
        self.address = address

    def add_record(self):
        res =  (self.name,self.contact_no,self.address)
        print("data recored:",res)

    def display(self):
        print("-------data display -----")
        print("employee's name:",self.name)
        print("employee's contact_no:",self.contact_no)
        print("employee's address:",self.address)

employee_1 = Employee("rahul","5876287683","22,d ox flat")
employee_1.add_record()

#✅ 5. Class with constructor that converts Celsius to Fahrenheit
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        f = (self.celsius * 9/5) + 32
        print(f"{self.celsius}°C = {f}°F")

t = Temperature(37)
t.to_fahrenheit()
      

    




