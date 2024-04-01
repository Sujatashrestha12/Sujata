# class Vehicle:
#     def __init__(self,name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price

#     def show(self):
#         print("Details; ", self.name, self.color, self.price)

#     def max_speed(self):
#         print("Vehicle max speed is 150")

#     def change_gear(self):
#         print("Vehicle change 6 gear")


# class Car(Vehicle):
#     def max_speed(self):
#         print("Car max speed is 240")
    
#     def change_gear(self):
#         print("Car change 6 gear")

# car = Car("Car x1", "Red", 200000)

# car.show()
# car.max_speed()
# car.change_gear()

#calculate the area of different shapes. We will create a base class shape with an area()method, and then create subclasses for specific shapes like rectangle, circle, and triangle which will override the area() method to calculate the area specific to each shape.

import math

class Shapes:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shapes):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        return self.length* self.breadth
    
class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
        return math.pi *self.radius**2
    
class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5* self.base *self.height
 #Creating instamces of different shapes.   
rectangle = Rectangle(5,4)
circle = Circle(3)
triangle = Triangle(6,8)
    
#Calculating areas without knowing specific types
print("Area of Rectangle: ", rectangle.area())
print("Area of a Circle: ",circle.area())
print("Area of Triangle: ",triangle.area())



      



    


        

