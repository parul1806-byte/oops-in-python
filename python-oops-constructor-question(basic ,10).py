
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

#✅ 5. Sum of two numbers using constructor
class add():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        print(f"the sum of numbers : {self.num1 + self.num2}")

number = add(34,89)
number_1 = add(56,45)
number.sum()
number_1.sum()

#✅ 6.Class with constructor that converts Celsius to Fahrenheit
class temp_convertor():
    def __init__(self,c):
        self.c = c
    def celsius_to_fahrenheit(self):
        f = (self.c *1.8)+32
        print("temp in fahrenheit:",f)
temp_1 = temp_convertor(57)
temp_2 = temp_convertor(45)
temp_1.celsius_to_fahrenheit()
temp_2.celsius_to_fahrenheit()

#✅ 7. Constructor that accepts 3 subject marks and calculates total
class total_marks():
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def sum(self):
        return self.m1+self.m2+self.m3
student_1 = total_marks("parul",67,78,23)
student_2 = total_marks("rahul",45,98,100)
print(f"Total marks of {student_1.name}:",student_1.sum())
print(f"Total marks of {student_2.name}",student_2.sum())

#✅ 8. Constructor that stores person’s age and checks if eligible to vote
class To_vote():
    def __init__(self,age):
        self.age = age
    def check_age(self):
        if self.age >= 18:
            print("you are eligible to vote ")
        else:
            print("you are not eligible to vote ")
age_1 = To_vote(67)
age_1.check_age()
age_2 = To_vote(16)
age_2.check_age()

#✅ 9. Create a class to reverse a string using constructor
class Reverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return self.text[::-1]

r = Reverser("Python")
print("Reversed:", r.reverse())

#✅ 10. Create a class to find the factorial of a number using constructor
class Factorial():
    def __init__(self,no):
        self.no = no
    def fact(self):
        if self.no == 1 or 0:
            print(f"the factorial of {self.no} is 1")
        else:
            res = 1
            for i in range(2, self.no+1):
                res *= i
            return res
no_1 = Factorial(5)
print(f"the factorial of {no_1.no}:",no_1.fact())






      

    




