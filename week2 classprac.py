# import random

# low_number = int(input("Enter a low number: "))
# high_number = int(input("Enter a high number: "))
# while high_number <= low_number:
#     print("high number must be grater than low number")
#     high_number = int(input("Enter a high number: "))
#
# n = random.randint(low_number, high_number)
# for i in range(n):
#     print(":)",end="")

"""
1.What are the three benefits of defining your own functions?
easy to debug,have control dool,more define and change function.

2.According to the differences in the return values of functions, into which two major categories can functions be classified?
Value-returning function（有返回值的函数）and
Non-value-returning function / Void function（没有返回值的函数）
The core lies in whether a result has been sent back through a return.
"""

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

"""
1.determine_grade
2.convert_usd_to_aud
3.print_report
4.calculate_average
5.is_even
6.get_valid_number
动作 + 对象 
Be clear and meaningful
example for 3:
is_positive → 是正数吗？
is_valid    → 是有效的吗？
is_empty    → 是空的吗？
is_adult    → 是成年人吗？
"""

"""
function must include doc string
On function
Parameter（参数/形式参数）= 定义函数时写的“变量名”
Argument（实际参数）= 调用函数时真正传进去的“值”

def add(a, b):
    return a + b

result = add(10, 20)
a,b = parameter
10,20 = argument
"""