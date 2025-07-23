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


