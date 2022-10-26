#This is a single line comment
#Variables and data types in python
from turtle import goto


name = input("Enter your name:")
age = input("How old are you?")
address = input("Enter your address")


print("About Me")
print("I am "+name+" .I am "+age+
"years old. I stay at "+address)

"""
This is a multiline comment
boolean operations in python
"""
print(True)
f_bool = False
print(f_bool)

#String operations
print("Harry What's going on") #string using double quotation marks
got_mark ='Game of thrones.....' #String using single quotation marks
print(got_mark)
print("$") # printing a single character

empty = ""
print(empty) #prints an empty line

multiple_lines = '''Triple quotes allows a 
multiline string
this is prove'''
print(multiple_lines)
print(multiple_lines)
random_string = "I am Batman"  # 11 characters
print(len(random_string))