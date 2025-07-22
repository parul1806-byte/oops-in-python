#Q1. Temperature Sensor
#Creating a class TemperatureSensor with private variable __celsius.
from traceback import print_list


class TemperatureSensor():
    def __init__(self,celsius):
        self.celsius = celsius

# getter for celsicus
    @property
    def celsius(self):
        return self.__celsius
#setter Allow setting temperature only between -50 and 150 Celsius.
    @celsius.setter
    def celsius(self,temp):
        if -50 <= temp <= 150:
            self.__celsius = temp
            print(f"temp in celsius :{self.__celsius}")
        else:
            print("temperature must be in btw -50 to 150")
            self.__celsius = 0
#Add a method get_fahrenheit() that returns the temperature in Fahrenheit.
#F = C * 9/5 + 32
    def get_fahrenheit(self):
        temp = (self.__celsius*1.8) + 32
        print(f"temp into fahrenheit:{temp} ")


temp1 = TemperatureSensor(56)
print(temp1.celsius)
print(temp1.get_fahrenheit())

#Q2. Email Validator:Create a class Employee with private variable __email.















'''
# .Create a Person class with: public name,protected _age,private __aadhar
class person():
    def __init__(self,name,age,aadhar):
        self.name = name
        self._age = age
        self.__adhar = aadhar

    def show_info(self):
        return self.name,self._age,self.__adhar


person1 =person("parul",23,23456789)
print(person1.show_info())
print(person1._person__adhar)# to acess private variables

#  Create a class Employee:Private __salary, Protected _department,Create getter and setter for salary.
class employee():
    def __init__(self,salary,department):
        self.__salary = salary ## private variable
        self._department = department # protected variable

    #getter
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):
        if value > 0:
            self.__salary = value
        else:
            print("invalid")
employee1 = employee(30000,"hr")
print(employee1.salary)
employee1.salary = 45000
print(employee1.salary)


#Create a Student class with private variables (__name, __age, __marks) and add getter/setter methods with proper validation for each.
class student():
    def __init__(self,name ,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
# getter and setter for name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,alpha):
        if alpha.isalpha():
            self.__name = alpha
        else:
            print("invalid name :name must be in alphabet")
            self.__name = "invalid name"
# getter setter method for age
    @property
    def age(self):
        return self.__age
    @ age.setter
    def age(self,value):
        if 5<= value <=100:
            self.__age = value
        else:
            print("age must be in between 0 to 100")
            self.__age = -1

#getter and setter method for marks
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,num):
        if 0 < num < 100:
            self.__marks = num
        else:
            print("marks should be between 0 to 100")
            self.__marks = -1


student1 = student("parul", 102, 45)
print(student1.name)
print(student1.age)
print(student1.marks)
'''

