# class Point:
#     def __init__(self,x=0.0,y=0.0):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other)-> float:
#         return Point(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f"{self.x},{self.y}"
#
#     def __lt__(self, other):
#         return self.x < other.x and self.y < other.y
#
#     def __gt__(self, other):
#         return self.x >other.x and self.y > other.y
#
#     def __ge__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def  __mul__(self, other):
#         return Point(self.x * other.x, self.y * other.y)
#
#     def __sub__(self, other):
#         return Point(self.x - other.x, self.y - other.y)
#
# here = Point(4.5,6.7)
# there = Point(6.7,5.9)
# print(here + there)
# print(here == there)
# print(here < there)
# print(here <= there)
# print(here > there)
# print(here >= there)
# print(here * there)
# print(here - there)



class Person:

    def __init__(self,name="",age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __eq__(self, other):
        return self.name == other.name

p1=Person("Ken",34)
p2=Person("Leo",54)

print(p1==p2)

