# import random
# #form random import
# from random import randint
#
# random_number = randint(10, 100)
#
# print(random_number)

AGE = 9

def main():
#     print_line("#",5)
#
#     age = calculate_sum(25,100)
#     print(age)
#
#     print(is_even(60))
#
#     movie_hour,movie_minutes = convert_movie_duration(289)
#     print(movie_hour,movie_minutes)
#
#     date_of_birth = (13,4,1976)
#     print(format_date(*date_of_birth))
#
# def format_date(day,month,year):
#     return f"{day}-{month}-{year}"
#
# def print_line(char="$",number=20):
#     print(char * number)
#
# def calculate_sum(age,number):
#     return age + number
#

    assert is_even(11)

def is_even(number):
    return number % 2 == 0
#
# def convert_movie_duration(movie_duration):
#     movie_hour = movie_duration // 60
#     movie_minutes = movie_duration % 60
#     return movie_hour, movie_minutes

    for i in range(0,101):
        print(f"{i} - {score_grade(i)}")

def score_grade(score):
    if score >= 85:
        grade = "HD"
    elif score >= 75:
        grade = "D"
    elif score >= 65:
        grade = "C"
    else:
        grade = "F"
    return grade
main()

import random
def main():
    low_number = int(input("Enter a number: "))
    high_number = int(input("Enter a number: "))
    while high_number <= low_number:
        print("high number must be greater than low number")
        high_number = int(input("Enter a number: "))


def read_file():
    in_file = open("read.txt")
    content = in_file.read()
    in_file.close()
    return content

print(read_file())