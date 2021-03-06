"""2. Define a class named Shape and its subclass Square. The Square class has an init function which
takes length as argument. Both classes have an area function which can print the area of the shape
where Shape’s area is 0 by default."""

class Shape:
    def __init__(self):
        pass
    
    def area(self):
        print("Area of Shape is: O")

class Square(Shape):
    def __init__(self):
        Shape.area(self)

    def area(self, leng):
        print("Area of squae is: ",leng*leng)


Sq = Square()
Sq.area(int(input("Enter a Length of Square: ")))