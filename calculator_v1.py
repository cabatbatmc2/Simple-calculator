#simple calculator app
from easygui import *

#Number 1
number_1 = integerbox("Number 1: ")

#Operator
operator = buttonbox("",choices = ["+", "-", "*", "/"])

#Number 2
number_2 = integerbox("Number 2: ")

#Addition
if operator == "+":
    answer = number_1 + number_2
    msgbox("Answer: " + str(answer))

# Subtraction
if operator == "-":
    answer = number_1 - number_2
    msgbox("Answer: " + str(answer))

#Multiplication
if operator == "*":
    answer = number_1 * number_2
    msgbox("Answer: " + str(answer))

#Division
if operator == "/":
    answer = number_1 / number_2
    msgbox("Answer: " + str(answer))   


