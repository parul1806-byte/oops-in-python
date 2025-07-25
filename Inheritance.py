#--------------------------------------------SINGLE INHERITANCE --------------------------
#1. Create a class Person with a method display_info() that prints name and age. Then create a child class Student that adds roll_number and a method display_student().
class Person():
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    def Display_Info(self):
        print(f"name :{self.name}\nage:{self.age}")
class Student(Person):
    def __init__(self,name,age,roll_number):
        self.roll_number = roll_number
        super().__init__(name,age) # inherit from class class person
    def Display_Student(self):
         print(f"student name :{self.name}\n student's age:{self.age}\n student's roll_no:{self.roll_number}")
student1 = Student("parul",45,56)
student1.Display_Info()
student1.Display_Student()

#2:Bank Account Inheritance
class Account():
    def __init__(self,balance):
        self.balance = balance

    def Show_Balance(self):
        print(f"current balance:{self.balance}")
class Saving_Account(Account):
    def __init__(self,balance):
        super().__init__(balance)
    def Add_Interest(self):
       print(self.balance +( self.balance * (5/100)))
b = Saving_Account(5000)
b.Add_Interest()

#3. Library System
class Libary_Item():
    def __init__(self,tittle ,author):
        self .tittle = tittle
        self.author = author
    def display_libary_item(self):
        print(f"Tittle:{self.tittle}\nauthor:{self.author}")
class Book(Libary_Item):
    def __init__(self,tittle,author,genre):
        self.genre = genre
        super().__init__(tittle,author)
    def book_detail(self):
        print(f"Tittle:{self.tittle}\nauthor:{self.author}\nGenre:{self.genre}")
book1 = Book("you and me","nick polo","sci-fi")
book1.book_detail()

#4.Employee Salary Calculator
class Employee():
    def __init__(self,name ,base_salary):
        self.name = name
        self.base_salary = base_salary
    def show_salary(self):
        print(f"Employe's Name :{self.name}\nEmploye's salary:{self.base_salary}")
class Software_eng(Employee):
    def __init__(self,name,base_salary):
        super().__init__(name,base_salary)
    def Calculate_salary(self):
         print("bonus salary:",(self.base_salary) + 2000)
employe1 = Software_eng("raj",30000)
employe1.show_salary()
employe1.Calculate_salary()

#5. Animal Sound Simulator
class Animal:
    def make_sound(self):
        print("some genric animal sound")

class Cat(Animal):
    def make_sound(self):
        print("meow is the sound of cat")

class Dog(Animal):
    def make_sound(self):
        print("bark is the sound of dog")

animal = Animal()
animal.make_sound()
animal = Cat()
animal.make_sound()
animal = Dog()
animal.make_sound()

#6.Ride Booking App:
class User():
    def __init__(self,user_name):
        self.user_name = user_name
        print(f"user name:{user_name}")
class Driver(User):
    def __init__(self,user_name,vehicle_name,vehicle_number):
        self.vehicle_name = vehicle_name
        self.vehicle_number = vehicle_number
        super().__init__(user_name)

    def info(self):
         print(f"user_name:{self.user_name}\nvehicle name:{self.vehicle_name}\nvehicle number:{self.vehicle_number}")
user1 = Driver("ram","B.M.W","x0455")
user1.info()

#-------------------------------------------------Multiple Inheritance--------------------------------------------------

# 7.Smart Home System
class light_System():
    def turn_on_light(self):
        print("lights turn on by light system")
class Security_System():
    def active_alarm(self):
        print("Security_System activate alarms")
class Smart_Home(light_System,Security_System):
    def system_status(self):
         print("smart home ")
         self.turn_on_light()
         self.active_alarm()

home = Smart_Home()
home.system_status()

#8.Digital Assistant
class weather():
    def get_weather(self,location):
        print(f"weather report in {location}")
class calenderRemainder():
    def set_remainder(self,event):
          print(f"Remainder set for the event:{event}")
class Assistant(weather,calenderRemainder):
    def display_info(self):
        print("assisting wheather and remainder")
        self.get_weather()
        self.set_remainder()
obj = Assistant()
obj.get_weather("delhi")
obj.set_remainder("cricket")
obj.display_info()