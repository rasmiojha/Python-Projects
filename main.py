class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive {self.model}")

    def stop(self):
        print(f"You stop {self.model}")

    def describe(self):
        print(f"Your have a {self.color} {self.model} of {self.year} ")

car1 = Car(model = "Mustang",year = 2024,color = "Red",for_sale = False)
car2 = Car("Corvet",2022,"Blue",False)
car3 = Car("Charger",2023,"Yellow",True)

# car1.describe()
# car1.drive()
# car1.stop()

# print(car1.model)
# print(car1.year)
# print(car1.for_sale)

class Employee:
    company_name = "Infosys Limited"
    no_of_count = 0
    def __init__(self,name,id,Dept,Location):
        self.name = name
        self.id = id
        self.dept = Dept
        self.location = Location 
        Employee.no_of_count +=1

emp1 = Employee("Spongebob",12349,"IVS-FS2","MCity")
emp2 = Employee("Patrick",23450,"CSI","NewYork")
emp3 = Employee("Squidward",89076,"FDS","Hoston")
emp4 = Employee("Darke",456788,"FINACLE","London")

# print(emp1.name)
# print(emp1.id)
# print(emp1.dept)
# print(emp1.location)
# print(Employee.no_of_count)

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")

class rat(Animal):
    def speak(self):
        print("Squak! Squak!")


dog = Dog("Scobby")
cat = Cat("Garfield")
rat = rat("Mickey")
# dog.eat()
# dog.sleep()
# dog.speak()
# cat.eat()
# cat.sleep()
# cat.speak()
# rat.eat()
# rat.sleep()
# rat.speak()

class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    
class Prey(Animal):
        def flee(self):
            print(f"{self.name} is fleeing")
class Predator(Animal):
        def hunt(self):
            print(f"{self.name} is hunting")

class Hawk(Predator):
    pass

class Rabbit(Prey):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

# rabbit.eat()
# rabbit.sleep()
# rabbit.flee()
# hawk.eat()
# hawk.sleep()
# hawk.hunt()
# fish.eat()
# fish.sleep()
# fish.flee()
# fish.hunt()

from abc import ABC,abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def start(self):
        pass
    @abstractclassmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car is started")
    def stop(self):
        print("Car is stopped")
class MotorCycle(Vehicle):
    def start(self):
        print("MotorCycle is Moving")
    def stop(self):
        print("Motorcycle is stopped")
# car1=Car()
# car1.start()
# car1.stop()

# motorcycle1 = MotorCycle()
# motorcycle1.start()
# motorcycle1.stop()

# class Shape:
#     def __init__(self,color,is_filled):
#         self.color = color
#         self.is_filled = is_filled
#     def describe(self):
#         print(f"It is a {self.color} and {'filled' if self.is_filled else 'not filled'}")

# class Circle(Shape):
#     def __init__(self,color,is_filled,radius):
#         super().__init__(color,is_filled)
#         self.radius = radius
#     def descriebe(self):
#         print(f"It is a {self.color} and {'filled' if self.is_filled else 'not filled'}")
# class Square(Shape):
#     def __init__(self,color,is_filled,width):
#         super().__init__(color,is_filled)
#         self.width = width
#     def describe(self):
#         print(f"It is a {self.color} and {'filled ' if self.is_filled else 'not filled'}")

# class Triangle(Shape):
#     def __init__(self,color,is_filled,width,height):
#         super().__init__(color,is_filled)
#         self.width = width
#         self.height = height
#     def describe(self):
#         print(f"It is a {self.color} and {'filled' if self.is_filled else 'not filled'}")

# circle1 = Circle("Red",True,5)
# square1 = Square("White",False,10)
# triangle1 = Triangle("Blue",False,10,15)

# circle1.describe()
# square1.describe()
# triangle1.describe()

from abc import ABC,abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self,width):
        self.width = width

    def area(self):
        return self.width * self.width
    
class Triangle(Shape):
    def __init__(self,width,height):
        self.width = width 
        self.height = height

    def area(self):
        return (self.height * self.width) /2
    
class Pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings


shapes = [Circle(5), Square(10), Triangle(5, 10), Pizza("Pepporoni", 10)]

# for shape in shapes:
#     print(f"{shape.area()} cm")

class Animal:

    Alive = True

class Dog(Animal):

    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):

    def speak(self):
        print("Meow! Meow!")

class Car:
    
    Alive = False

    def speak(self):
        print("Honk! Honk!")

animals =[Dog(),Cat(),Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.Alive)

class Library:

    def __init__(self,name):
        self.name = name
        self.books = []

    def add_books(self,book):
        self.books.append(book)
    
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

library = Library("New work Public Library")

book1 = Book("Harry Potter", "J .K.Rowling")
book2 = Book("The Hobbit", "J.R.R Tolkin")
book3 = Book("The color of Magic", "Terry Prat")

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

# print (library.name)
# print(book1.title )

# for book in library.list_books():
#     print(book)

class Engine:

    def __init__(self,horse_power):
        self.horse_power = horse_power

class Wheel:
    
    def __init__(self,size):
        self.size = size

class Car:
    def __init__(self,make,model,horse_power,wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheel_size = [Wheel(wheel_size) for _ in range(4)]
    
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) Wheel size:{self.wheel_size[0].size} in"
    
car1 = Car("Ford","Mustang",500,18)
car2 = Car("Chevrolet","Corveet",670,19)

# print(car1.display_car())
# print(car2.display_car())

class Company:

    class Employee:
        def __init__(self,name,position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self,company_name):
        self.company_name = company_name
        self.employees = []
    
    def add_employee(self,name,position):
        new_employee = self.Employee(name,position)
        self.employees.append(new_employee)

    def list_employee(self):
        return [employee.get_details() for employee in self.employees]

company1 = Company("Krusty Krab")
company2 = Company("Chum Bucket")

company1.add_employee("Eugene", "Manager")
company1.add_employee("Spongebob", "Cook")
company1.add_employee("Squid ward", "Cashier")

company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "Assitance")

# print(company2.company_name)
# for employee in company2.list_employee():
#     print(employee)

class Employee:

    def __init__(self,name, position):
        self.name = name 
        self.position = position 

    def get_details(self):
        return f"Employee name is {self.name} and his position is {self.position}"
    

    @staticmethod
    def is_valid_position(position):
        valid_position = ["manager","cook", "Cashier"]
        return position in valid_position
    
emp1 = Employee("Eugene","Manager")
emp2 = Employee("Squid ward","Cashier")
emp3 = Employee("Spongebob", "Engineer")

# print(Employee.is_valid_position("Rocket Engineer"))
# employees = [emp1,emp2,emp3]
# for emp in employees:
#     print(emp.get_details())


class Student:
    count = 0
    cgpa = 0
    def __init__(self,name,cgpa):
        self.name = name 
        self.cgpa = cgpa
        Student.count += 1
        Student.cgpa += cgpa


    def get_details(self):
        return f"{self.name} {self.cgpa}"
    
    @classmethod
    def get_count(cls):
        return f"{cls.count}"
    
    @classmethod
    def calculate_average(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.cgpa/cls.count:.2f}"

stud1 = Student("Spongeboob",8.5)
stud2 = Student("Patrick",2.0)
stud3 = Student("Sandy", 4.8)
stud4 = Student("Carl",4.9)

print(Student.get_count())
print(Student.calculate_average())