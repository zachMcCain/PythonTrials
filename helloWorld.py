print("Hello World")

character_name = "Sam"
is_male = True
character_age = 50
print("What is your name?")
print("My name is", character_name[0])
print(is_male)
print(character_age)
print(character_name.index("am"))
print(character_name.replace("am", "imon"))

my_number = 25
my_negative = -2
print(str(my_number) + " my favorite number")
print(abs(my_negative))
print(pow(3, 2))
print(max(4, 29))
print(min(4, 29))
print(round(4.594))


from math import *
print(floor(4.939))
print(ceil(4.939))
print(sqrt(4.939))

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = int(num1) + float(num2)
print(result)

friends = ["David", "Anthony", "Garrett", "Graham"]
print(friends[-2])
print(friends[1:])
friends[2] = "Josh"
print(friends[1:3])