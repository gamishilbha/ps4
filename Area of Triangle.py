"""
Python assignment 4
Program 1.1 Area of triangle using class concept
"""
class Triangle:
    def __init__(self):
        a=input("What is the value of a?\n")
        self.a=int(a)
        b=input("What is the value of b?\n")
        self.b=int(b)
        c=input("What is the value of c?\n")
        self.c=int(c)
    def __str__(self):
        return "%s, %s and %s are the given inputs" %(self.a, self.b, self.c)

class Area(Triangle):
    def __init__(self, *args):
        super(Area, self).__init__(*args)
        s=(self.a+self.b+self.c)*.5
        self.area_triangle=(s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    def __str__(self):
        return "The area of the triangle for the given side lengths %s, %s and %s is : %s" %(self.a, self.b, self.c, self.area_triangle)

values=Area()
print(values)
