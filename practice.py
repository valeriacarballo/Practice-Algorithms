#Create a function that takes two numbers as arguments and return their sum.
def addition(a, b):
    return a+b

#Create a function that takes a number as an argument, increments the number by +1 and returns the result.
def increment(a):
    return a+1

#Write a function that takes an integer minutes and converts it to seconds.
def min_to_sec(minutes):
    return str(minutes*60) + 's'

#Write a function that takes the base and height of a triangle and return its area.
from fractions import Fraction
def area_triangle(b, h):
    area = Fraction(1, 2) *b*h
    return area

#Write a function that converts hours into seconds.
def hr_to_sec(hours):
    return str(hours * 60 * 60) + 's'

# There is a single operator in Python, capable of providing the remainder of a division operation. 
# Two numbers are passed as parameters. 
# The first parameter divided by the second parameter will have a remainder, possibly zero. 
# Return that value.
def remainder(a,b):
    return a%b

#Create a function that takes a list and returns the first element.
def first_element(array):
    return array[0]

#Create a function that takes a base number and an exponent number and returns the calculation.
def exponent(base, exponent):
    return base**exponent

#In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. 
#The farmer breeds three species:
#chickens = 2 legs
#cows = 4 legs
#pigs = 4 legs
#The farmer has counted his animals and he gives you a subtotal for each species. 
#You have to implement a function that returns the total number of legs of all the animals.
def get_legs(x, y, z):
    chickens = 2
    cows = 4
    pigs = 4
    number_legs = x*chickens + y*cows + z*pigs
    return number_legs


def get_container(food: str):
    if food == "beer":
        return "bottle"
    if food == "bread":
        return "bag"
    if food == "candy":
        return "plastic"
    if food == "cheese":
        return None

#person_input = input("Container for:")
#container = get_container(person_input)
#print(container)


#Write two functions:
#to_int() : A function to convert a string to an integer.
#to_str() : A function to convert an integer to a string.
def to_str(integer: int):
    return str(integer)

def to_int(string: str):
    return int(string)

#Create a function that takes a number as its only argument and returns True if it's less than or equal to zero, otherwise return False.
def zero(number: int):
    if number <= 0:
        return "True"
    else:
        return "False"

#Create a function that takes a number as an argument, increments the number by +1 and returns the result.
numbers = [0, 1, 2, 3, 4]
new = []
for number in numbers:
    new.append(number + 1)

#Create a function that takes a list of numbers and returns the smallest number in the list
list_numbers = [6, 8, 12, 3, 9, 17]
def find_smallest_num(numbers: list):
    numbers.sort()
    return numbers[0]

#Create a function that takes a list of numbers. Return the largest number in the list
def find_largest_num(numbers: list):
    numbers.sort()
    return numbers[len(numbers)-1]

#Given a list of integers, return the difference between the largest and smallest integers in the list.
integers = [27, 82, 3, 6, 54, 89, 900, 23]
def difference(integers: list):
    return find_largest_num(integers) - find_smallest_num(integers)

#Create a function that returns True if an integer is divisible by 5, and false otherwise.
def divisible_by_5 (number: int):
    if number%5 == 0:
        return True
    else:
        return False

#Given an array of numbers return a new array so that the odd numbers are all first then the even numbers

numbers = [1, 2, 3, 4, 5]

even = []
odd = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
odd_even = odd + even

#How do you find the missing number in a given integer array?
    # make an array from 1-100 and remove an element
hundred = []
for i in range(1, 101):
    hundred.append(i)
hundred.remove(hundred[5])

    # find missing number
def sum_array(n: int):
    sum = n*(n+1)/2
    return sum
missing_number = sum_array(100) - sum(hundred)
