# def main()
#     filename = input("")
#
# FILENAME = "read.txt"
# in_file = open(FILENAME)
# content = in_file.readline()
#
# in_file.close
#
# print(content)

# out_file = open("demo.txt", "w")
# print("I like Python",file = out_file)
# out_file.close()

# out_file = open("demo.txt", "a")
# print("I love Python")
# out_file.close()

# countries = ["Italy","Germany","United Kingdom"]
# out_file = open("demo.txt", "a")
# out_file.write(countries)

# s = "\tPython, Monty \n"

# print(s)
# print(s[1],".",sep="")
# print(s.strip(),".",sep="")
# print(s.replace('','*'))
# print(s.lstrip(),".",sep="")
# print(s.strip().split(','))
# print(list(s))

# name = input("Name: ")
#
# s = "\t"+ name +" \n"
#
# print(s)
# print(s[1],".",sep="")
# print(s.strip(),".",sep="")
# print(s.replace('','*'))
# print(s.lstrip(),".",sep="")
# print(s.strip().split(','))
# print(list(s))
#
# out_file = open("name.txt","w")
# print(s.strip(), file=out_file)
# out_file.close()
#
# print("Done")

# name = ["Bob","Amy","Tom"]
#
# position = 1
#
# for name in name:
#     file_name = name + ".txt"
#     out_file = open(file_name,"w")
#     print(position,file=out_file)
#     out_file.close()
#
# position += 1
#
# print("Done")

# print(10/0)
#
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Program cannot devied by 0")

# name = "Lea"
# try:
#     print(name)
# except NameError:
#     print("Variable name is not found")

# try:
#     number = int(input("Enter a number"))
#     print(200/number)
# except ValueError:
#     print("Cannot divide by 0")
# except ZeroDivisionError:
#     print("Input must be a number")
#
# print("Finished")

# def lbyl():
#     "Look Before Your Leap Version"
#     text = "123"
#     if not isinstance(text, str):
#         return None
#     else:
#         return text

