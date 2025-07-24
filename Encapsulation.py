import random
import warnings
#Q1. Temperature Sensor
#Creating a class TemperatureSensor with private variable __celsius.
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
class Employee():
    def __init__(self,Email):
        self.Email = Email

    # getter function to return the email
    @property
    def Email(self):
        return self.__Email

    #setter function: email must contain @ and endswith .com
    @Email.setter
    def Email(self,id):
        if "@" in id and id.endswith(".com"):
            print("It is a vaild email")
            self.__Email = id
        else:
            warnings.warn("It is not a valid email, enter a valid email ")
            self.__Email = "invalid@invalid"
#creating object and calling the class
employee1 = Employee("parulpal7088@gmail.com")
print("stored email",employee1.Email)
employee2 = Employee("rahul678")
print("stored email:",employee2.Email)


#Q3. Quiz Score Tracker
#Creating a Quiz class with private list __scores.
class Quiz():
    def __init__(self,score,):
        self.__score = []

    # getter to return total score :
    @property
    def score(self):
        return self.__score
    #setter method
    def add_score(self,score_no):
        if 0<= score_no <=100:
            self.__score.append(score_no)
        else:
            print("score should in btw 0 to 100")
    # to calculate avg
    def avg(self):
        if self.__score:
            return sum(self.__score) / len(self.__score)
        else:
            return None

q1 = Quiz(0)
q1.add_score(20)
q1.add_score(45)
q1.add_score(56)
q1.add_score(680)
print("final score:",q1.score)
print("average of score:",q1.avg())

#Q4 Playlist Manager
#Creating a class called Playlist that manages a list of songs.
class Playlist():
    def __init__(self,songs):
        self.__songs = [] # list that will store songs

    # getter to get the list of songs
    @property
    def songs(self):
        return self.__songs
    # method to add songs --> setter
    def Add_Songs(self,song_name):
        if song_name in self.__songs:
            print(f"{song_name}, This song is alredy exists")
        else:
             self.__songs.append(song_name)
    # method to remove a song
    def Remove_Song(self,song_name):
        if song_name in self.__songs:
            self.__songs.remove(song_name)
        else:
            print("This song didn't exists")
    # method to calculate the total song
    def Total_Songs(self):
        print("Total songs in the playlist :",len(self.__songs))
p1 = Playlist(0)
p1.Add_Songs("shape of you")
p1.Add_Songs("pretty little baby")
p1.Add_Songs("believer")
p1.Add_Songs("shape of you")
p1.Remove_Song("believer")
p1.Add_Songs("you and me")
p1.Add_Songs("you and me")
print("PLAYLIST:",p1.songs)
p1.Total_Songs()

#Q5 Vehicle Speed Control
#Creating a Vehicle class with private variable __speed.
class Vehicle ():
    def __init__(self,speed):
        self.speed = speed
    # getter
    @property
    def speed(self):
        return self.__speed
    #setter '
    @speed.setter
    def speed(self,speeds):
        if speeds > 120:
            warnings.warn("over speed")
        self.__speed = speeds

    # method to add certain value to the speed
    def add_speed(self):
         self.__speed += 20
         return self.__speed

s1 = Vehicle(56)
print("initial speed: ",s1.speed)
print("speed after a value :",s1.add_speed())
s2 = Vehicle(560)
print("initial speed: ",s2.speed)
print("speed after a value :",s2.add_speed())

#6 .Create a Person class with: public name,protected _age,private __aadhar
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

# 7 Create a class Employee:Private __salary, Protected _department,Create getter and setter for salary.
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


# 8Create a Student class with private variables (__name, __age, __marks) and add getter/setter methods with proper validation for each.
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

#9Password Validator :Creating a UserAccount class with private variable __password.
class UserAccount():
    def __init__(self,password):
        self.password = password
# getter to retun the password
    @property
    def password(self):
        return self.__password
#setter for conditions
    @password.setter
    def password(self,pas):
        if (len(pas)>8 and
                any(char.isalpha() for char in pas) and
                any(char.isdigit() for char in pas) and
                any(char in "@#$%" for char in pas)):
            self.__password = pas
            print(f"{pas}: it is a valid pass")
        else:
            print(f"{pas}:week password")

user1 = UserAccount("parulpal16@")
user2 = UserAccount("1234")

#10 Parcel Weight Handler
class Parcel():
    def __init__(self,weight):
        self.weight = weight
#getter
    @property
    def weight(self):
        return self.__weight
#setter:Weight must be between 0.5kg and 50kg.
    @weight.setter
    def weight(self,mass):
        if 0.5<= mass <= 50:
            self.__weight = mass
        else:
            warnings.warn("invalid weight , weight must be in given range")
# method for shipping cost
    def shipping_cost(self):
        cost = self.__weight*20
        return cost
parcel1 = Parcel(45)
print("weight :",parcel1.weight)
print("shopping cost",parcel1.shipping_cost())
parcel2 = Parcel(56)

#11 Booking Limit Tracker , Class: Booking with private var __seats.
class Limit_Tracker():
    def __init__(self):
        self.seats = 0

# getter
    @property
    def seats(self):
        return self.__seats
#setter
    @seats.setter
    def seats(self,limit):
        if 0 <= limit <= 100:
            self.__seats = limit
        else:
            print("limit exceeds")
    def book(self,new_seats):
        if self.__seats+new_seats > 100:
            print("booking exceeds")
        else:
            self.__seats+= new_seats
            print(f"total seat book:{self.__seats}")
b1 = Limit_Tracker()
b1.book(56)
b1.book(20)
b1.book(45)

#12. Unique User ID Generator:Creating  User class with private __username.
class User():
    def __init__(self,user_name):
        self.user_name = user_name
#getter
    @property
    def user_name(self):
        return self.__user_name
#setter username must:Start with a letter,Be alphanumeric,Be at least 6 chars
    @user_name.setter
    def user_name(self,name):
        if (len(name)>=6 and name[0].isalpha() and
            any(char.isalpha() for char in name)and
            any(char.isdigit() for char in name)):
            self.__user_name = name
            print(f"{name}:this user_name is 100% valid")
        else:
            print("invalid user_name")
            self.__user_name = None


    def Genrate_id(self):
        if self.__user_name:
            randon_num = random.randint(100,999)
            return self.__user_name + str(randon_num)
        else:
            print("error")

user1 = User("parul7088")
print("ID:",user1.Genrate_id())
user2 = User("parul")
print("ID:",user2.Genrate_id())

#13. Course Grade Average, Creating Course class with private __grades (a list).
class Grade():
    def __init__(self):
        self.__grades = []# empty lis
# getter to get the grades
    @property
    def grades(self):
        return self.__grades
#setter method to add the grades
    def Add_Grades(self,marks):
        if marks in range(0,101):
            self.__grades.append(marks)
            print(f"{marks}:added")
        else:
            print("Invalid marks")

# method for average
    def Avg(self):
        if self.__grades:
            return sum(self.__grades)/len(self.__grades)
        else:
            warnings.warn("Error!!! , marks should be range of 0 to 100")
s1 = Grade()
s1.Add_Grades(67)
s1.Add_Grades(45)
s1.Add_Grades(21)
print("GRADES:",s1.grades)
print("average:",s1.Avg())


#14Login Attempts Blocker:Class: LoginSystem
class LoginSystem():
    def __init__(self,password):
        self.__password = password
        self.attempts = 0
    @property
    def password(self):
        return self.__password
    def login(self,input_password):
        if self.attempts > 3 :
            print("blocked")
            return
        if input_password == self.__password:
            print("password accepted")
            self.attempts = 0
        else:
            self.attempts += 1
            print("wrong password")
            if self.attempts == 3 :
                print("blocked")
person1 = LoginSystem("12345@@")
print("password for person1:",person1.password)
person1.login("1234")
person1.login("4567")
person1.login("12345@@")







