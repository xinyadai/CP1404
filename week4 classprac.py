# names=["Lukas","Lea"]
# print(names)
#
# try:
#     print(names[2])
# except IndexError:
#     print("no")
# print(names[0])
# print(names[2])
# print(names[-1])
# for name in names:
#     print(name)

# numbers = [4,6,3,78,26]
# numbers.append(45)
# print(numbers)
#
# del numbers[2]
# print(numbers)
#
# numbers.remove(26)
# print(numbers)
#
# numbers.reverse()
# print(numbers)
#
# numbers.sort()
# print(numbers)
#
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# data = ["Lea",34],["Sam",24],["Eve",67]
# print(data[0][1])
# data.sort(key = itemgetter(1),reversw = True)
# print(data)


# words = "This is Python"
# print(words)
# words = words.split()
#
# print([word for word in words if len(word)>2])
# print([len(word) for word in words])
# print([word.upper() for word in words])

# cars = [["Audi",2006],["BMW",2016],["Jaguar",2026]]
# print([tuple(car) for car in cars])
# print([car[0] for car in cars])
# print([car[1] * 2 for car in cars])
# print(min((car[1]) for car in cars))


# print(words)
#
# words.append("is")
# print(words)
# print([word for word in words])


# numbers = [23,67,45,23]
# new_numbers = []
#
# for number in numbers:
#     total = numbers * 2
#     new_numbers.append(total)
#
# print(new_numbers)
#
# print([number * 2 for number in numbers if number >50])


# x = 5
# y = 6
#
# print(x==y)
#
# numbers = [12,45,67]
# new_numbers = numbers
# print(new_numbers)
#
# print(numbers is new_numbers)
#
# numbers_2 = [12,45,67]
# print(numbers is numbers_2)
#
# numbers.append(55)
# print(numbers)
# print(new_numbers)
# print(numbers_2)


# things = []
# for x in range (1,4):
#     for y in range (1,4):
#         things.append(x + y)
#
# print(things)
#
# print([x+y for x in range(1,4) for y in range(1,4)])

# names = ["Ada","Alan","Bill","John"]
# print(",".join(names))
# name_to_remove = input("Who do you want to remove? ").title()
# while name_to_remove != "":
#     try:
#         names.remove( name_to_remove )
#     except ValueError:
#         print("")
#         print(names)
#     name_to_remove = input("Who do you want to remove? ").title()
# print("good try")

# with open ("numbers. txt", "r") as input_file:
#     numbers = input_file.readlines()
#     sum_of_numbers = 0
#     for number in numbers:
#         sum_of_numbers += float (number)
# print(f"Total sum of numbers is {sum_of_numbers}")


# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
#
# # for item in data:
# #     name = item[0]
# #     score = item[1]
# #     print(name,"=",score)
# #
# sorted_data = sorted(data)
# for pair in data:
#     name, score = pair
#     print(f"{name:<{20} = {score:>{5}}")


def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_number(numbers)

def square_numbers(numbers):
    for i in range (len(numbers)):
        numbers[0] = float(numbers[0]) ** 2

def display_number(numbers):
    numbers.sort()
    print(".".join(str(number) for number in numbers))
    print(".".join(str(number) for number in sorted(numbers)))

def get_numbers():
    text = input("Enter numbers separated by commas: ")
    numbers = text.split(',')
    return numbers

main()