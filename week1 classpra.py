"""
get gifts
get students
average_of_number= gifts // students
residue_of_number =gifts % students
display average_of_number
display residue_of_number
"""
# gifts = int(input("Enter the number of gifts"))
# students = int(input("Enter the number of students"))
# each_students_number = gifts // students
# residue_of_number = gifts % students
# print(each_students_number)
# print(residue_of_number)

"""
1.if,else,else
2.if
3.if,elif,else
4.if,else
5.if,elif,else
"""

"""
get item_price
get has_GST
if has_GST(y/n) == y:
    final_price = item_price * 1.1
else:
    final_price = item_price
    
display final_price
"""
# item_price = float(input("Enter item price: $"))
# has_GST = input("Do you have GST? (y/n): ")
# if has_GST == "y":
#     final_price = item_price * 1.1
# else:
#     final_price = item_price
# print(f"${final_price:.2f}")

"""
1.for
2.while
3.for
4.for
5.while
6.for
"""
# number = int(input("Enter a number: "))
# count = 1
# while count <= number:
#     print(count)
#     count += 1
#
# number = int(input("Enter a number: "))
# for i in range(1, number+1):
#     print(i)


# SECRET_NAME = 5
# use_number = int(input("Enter a number to 1-10:"))
# while use_number != SECRET_NAME:
#     print("It not correct please try again")
#     use_number = int(input("Guess again:"))
#
# print("Correct!You guess the secret name.")

# user_name = input("Enter your name: ")
# while user_name == "":
#     print("Name cannot be blank")
#     user_name = input("Enter your name: ")
#
# user_salary = float(input("Enter your salary: "))
# while user_salary < 0:
#     print("Salary cannot be below zero")
#     user_salary = float(input("Enter your salary: "))
#
# print("Name:",user_name.upper())
# print(f"Salary: ${user_salary:,.2f}")

user_number = int(input("Have many age?: "))

total = 0
for i in range(user_number):
    age = int(input("Enter your Age: "))
    total += age

average = total / user_number
print(total)
print(average)

age = int(input("Enter your Age: "))
total = 0
count = 0

while age != -1:
    total += age
    count += 1
    age = int(input("Enter your Age: "))

average = total / count
print(total)
print(count)