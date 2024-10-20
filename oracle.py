# import cx_Oracle
# con = cx_Oracle.Connection('user1/pswd1@10.123.79.58/Georli03')
# cur = cx_Oracle.Cursor(con)
# cur.execute("INSERT INTO Computer VALUES (1005,'Dell','Vostro',2013)");
# print(cur.rowcount)
# cur.close()
# con.commit()
# con.close()


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width * self.width

class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 0.5 * self.width * self.height

class Pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings

shapes = [Circle(5), Square(10), Triangle(5, 10), Pizza("Pepperoni", 10)]

for shape in shapes:
    print(f"{shape.area()} cm²")
