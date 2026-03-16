# monsters = [["Mike",340,"blue"],["James",14,"green"],["Randall",24,"purple"]]
#
# scary_monster = [monster for monster in monsters if monster[1] > 16]
# print(scary_monster)



# class Student:
#     def __init__(self,name="",student_id=0):
#         self.name=name
#         self.student_id=student_id
#
#     def __str__(self):
#         return f"{self.student_id} is {self.name}"
#
# # sl = Student("Lukas","12345")
# print(sl)
#
# s2 = Student("Lea","34567")
# print(s2)
#
# # print(f"{s2.name} id is {s2.student_id}")
#
# name = input("Enter your name: ")
# student_id = int(input("Enter id: "))
#
# sl = Student(name,student_id)
# print(sl)


# class Monster:
#     def __init__(self, name="Mike",number_of_teeth=0,colour="blue"):
#         self.name = name
#         self.number_of_teeth = number_of_teeth
#         self.colour = colour
#
#     def is_scary(self):
#         return self.number_of_teeth > 16 or self.colour == "red"
#
#     def __str__(self):
#         return f"{self.name} {self.number_of_teeth} {self.colour} {self.is_scary()}"
#
# # ml = Monster("Cliff",25,"blue")
# # print(ml)
#
# monsters = [["Mike",340,"blue"],["James",14,"green"],["Randall",24,"purple"]]
#
# scary_monsters = [monster for monster in monsters if monster.is_scary()]
# for monster in scary_monsters:
#     print(scary_monsters)
#
# print(scary_monsters)



# class User:
#     def __init__(self, name):
#         self.name = name
#         self.number_of_tacos = 5
#         self.score = 0
#
#     def give_taco(self,other_user):
#         if self.number_of_tacos > 0:
#             self.number_of_tacos -= 1
#             other_user.score += 1
#         else:
#             print(f"No more Taco left to give")
#
#     def __str__(self):
#         return f"{self.name},{self.score} points,{self.number_of_tacos} tacos left"