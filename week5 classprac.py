# from operator import itemgetter
#
# data = [['Derek',7],['Xavier',80],['Bob',612],['Chantanelle',9]]
# name_width = max(len(pair[0])for pair in data)
# score_width = max(len(str(pair[1]))for pair in data)
#
# data.sort(key=itemgetter(1),reverse =True)
#
# for pair in data:
#     name,score = pair
#     print(f"{name:< {name_width}} = {score:>{score_width}}")
#
# name = ["Ada","Sam","Tim"]
# print("%".join(name))


# name_to_age = {"Bill": 21,"Jane": 34,"Sven": 56}
# print(name_to_age)
#
# name = input("Enter name: ")
# age = int(input("Enter age: "))
#
# name_to_age[name] = age

# print(name_to_age)
#
# print(name_to_age.keys())
# print(name_to_age.values())
# print(name_to_age.items())
#
# print(max(name_to_age.values()))
#
# for name in name_to_age:
#     print(f"{name} is {name_to_age[name]}")
#
# print()
#
# print("".join(f"{name} is {name_to_age[name]}\n" for name in name_to_age))
#
# print()
#
# for name, age in name_to_age.items():
#     if age > 25:
#         print(f"{name} is {age}")

# print(name_to_age["Jane"])
# print(len(name_to_age))
#
# name_to_age["Lukas"] = 20
# print(name_to_age)
#
# name_to_age["Lukas"] = "ten"
# print(name_to_age)
#
# name_to_age["Lukas"] = 24
# print(name_to_age)
#
# name_to_age["Jane"] = name_to_age["Sven"]
# print(name_to_age)
#
# for name in name_to_age:
#     print(name)



# word_to_count = {"apple": 4,"Kiwi": 8}
# words = ["apple","orange"]

"""Look before you lean"""
# for word in words:
#     if word in word_to_count:
#         word_to_count[word]= word_to_count[word] + 1
#         print(word,word_to_count[word])
#     else:
#         word_to_count[word] = 1
#         print(word,word_to_count[word])

"""EASP"""
# for word in words:
#     try:
#         word_to_count[word] = word_to_count[word] + 1
#         print(word,word_to_count[word])
#     except KeyError:
#         word_to_count[word] = 1
#         print(word,word_to_count[word])

"""get method"""
# for word in words:
#     word_to_count[word] = word_to_count.get(word,0) + 1
#     print(word,word_to_count[word])



# module_to_number ={"CP1401": 45,"CP1404": 78,"CP5639": 34}
# modules = ["CP1401","CP1404","CP5639"]
#
# for module in modules:
#     module_to_number[module] = module_to_number.get(module,0) + 1
#     print(module,module_to_number[module])



# subjects = """
# CP1401
# CP5639
# CP1404
# CP1401
# """
#
# print(subjects)
# print(subjects.split())
# print(set(subjects.split()))
#
# # list_example = []
# # dictionary_example = {}
# example = set()
# print(type(example))
#
# example.add("apple")
# print(example)
#
# example.add(1)
# print(example)
#
# example.add(8)
# print(example)
#
# example.add(False)
# print(example)
#
# example.pop()
# print(example)



# my_subjects = {"CP1401","CP5966","CP1404"}
# your_subjects = {"CP1401","CP5369","CP1404"}
#
# print(f"Union = {my_subjects | your_subjects}")
# print(f"Difference = {my_subjects - your_subjects}")
# print(f"Intersection = {my_subjects & your_subjects}")
# print(f"Symmetric Difference {my_subjects ^ your_subjects}")



# name_to_age = {"Lea"_:45,"Evelyn"_:78}
# print({name: age * 2 for (name,age)in name_to_age.items()})
#
# print({name: age * 2 for (name,age)in name_to_age.items() if age == max(name_to_age.values())})



# flowers = ("cala lily","rose","rose","tulip")
# numbers = {34,56,12,90}
#
# print(dict(zip(flowers,numbers)))
# print(list(zip(flowers,numbers)))
# print(tuple(zip(flowers,numbers)))

# import json
#
# name_to_age = {"Lea": 45,"Evelyn": 78}
# json_name_to_age = json.dumps(name_to_age)
#
# print(json_name_to_age)



# name_to_age = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
# name_width = max((len(name) for name in name_to_age.keys()))
# age_width = max((len(str(age)) for age in name_to_age.values()))
#
# print(age_width)
#
# for name,age in sorted(name_to_age.items(),key=itemgetter(1),reverse=True):
#     print(f"{name}: {age}")



def main():
    flowers = ["cala lily","rose","tulip"]
    print(convert_string_to_dictionary(flowers))

def convert_string_to_dictionary(flowers):
    flower_to_length = {}
    for flower in flowers:
        flower_to_length[flower] = len(flower)
    return flower_to_length

def comprehension_to_dictionary(flowers):
    return{flower:len(flower) for flower in flowers}
main()