
import math

print ("examples:")
print (2+3)
print (2*3)
print (2**3)
print (2/3)
print (2%3) # % is the modulo; returns remainder of dividing left side by right side

# array l
l = [1, 2 ,3 ,4 ,5]
# print the 4th element of the array
print(l[3])
# print the length of the array
print(len(l))
#add 6 to the array
l.append(6)
print(l)


# Definitions
    # variables : store values
    # int : no fractional part
    # float : number w fractional part
    
    # sequences: ordered elements; strings, tuples, lists
    # sets : unordered elements

    # operators : symbols to carry out operations; arithmetic (+, -, *, /, %, **, //), assignment (=, +=, -=, *=, /=, **=, //=), logical (or, and, not), relational (<, <=, >=)

    # ceil : round up
print (math.ceil(2.687))

    # fabs : absolute value
print (math.fabs(-2.45))

    # factorial(x)
print (math.factorial(6))

    # floor : round down
print (math.floor(2.687))

from fractions import Fraction # helps to deal with fractions
print (Fraction(4, -16))

# ------------------------------
# strings : predefined objects with characters

name = "Valeria"
    # the value at a particular location of a string can be displayed using indexing; <name of string>[index]
print (name[0])
print (name[-2]) # negative indexing provides nth position starting from the end
name = name + " Carballo"
print(name)

    # slicing : removing part of a string
name = name[2:] # removes letters before 2nd index
print (name)

name = name[:2] # removes 2nd index and those after
print (name)

# ------------------------------

# lists (arrays) : collection of objects; homogeneous (similar elements; ex. all number) or heterogeneous (different elements; ex. strings and numbers) 
# tuples : contains elements that can be treated individually or as a group

fruits = ("apple", "orange", "mango", "banana")
(x,y,z,d) = fruits
print(x)

# ------------------------------
# general format:
# if <test condition>:
    # <block if the test condition is true> 

# if <test condition>:
    # <block if the test condition is true>
# else:
    # <block if the test condition is not true>

score = input("Enter marks : ") #input is a way to interact w user; requests an input from user in terminal
if int(score)>40:
    print('pass')
else:
    print('fail')
 

name = input("What is your name?:")
if name == 'David':
    print('I love you')
else:
    print("Goodbye")







