
# Quadratic Equation
# Equation = (-b +- sqrt(b^2-4ac)) / 2a
# Make a couple functions that solve the above
# You will receive
# - b
# - a
# - c
import math

def quadratic(a, b, c):
    part_3 = b**2 - 4*a*c
    if part_3 < 0:
        i_1 = str(math.sqrt(abs(part_3))) + "i"
        part_5 = str(-b) + " +- " + i_1
        part_6 = part_5 + " / " + str(2*a)
        return part_6


    part_2 = math.sqrt(part_3)
    part_1 = -b + part_2
    part_4 = part_1 / 2*a
    
    return part_4

result = quadratic(7, 30, 5)
print(result)


# string = a letter or sequence of lleters in programming
# ex:
#  - "i"
#  - "Hy my name is David"

#  int = a representation of numbers (integrers)
#  ex:
#  - 1
#  - 123


# pythagorean theorem: c**2 = a**2 + b**2
# c = sqrt(b**2 + a**2)

import math

def pythagorean(a, b):
    part_1 = a**2 + b**2
    part_2 = math.sqrt(part_1)
    return part_2

result = pythagorean(2, 4)






