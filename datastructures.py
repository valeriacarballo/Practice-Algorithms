'''
Data Structure: HASHMAP
Definition: Data structure that maps key to value. 

            In python its known as a dictionary, why? because a dictionay has the following structure.
            - "Word": "Definition" ex. "smart": "Someone who know stuff"
            In this scenario "smart" is the key & "Someone who know stuff." is the value
            aka. key-value data structure

Complexity:
    - Search: O(1) - constant
    - Add: O(1) - constant # There is no order just need key and value
    - Delete: O(1) - constant # There is no order, just need key to delete

Representation: 
    - Brackets {} are used to create an empty dictionary
    - Think of {} as like encapsulation of something

2 Sum Problem: 
   - input [1,2,3]
   - target 4 
   - return [0,2]

'''

# two sum problem using for loops: 0f(n) = n**2 (quadratic time)

def twoSum(nums: list, target: int):
    for p1 in range(len(nums)):
        for p2 in range(len(nums)):
            y = p2 + 1 
            if y >= len(nums):
                break
            if y == p1:
                continue
            if nums[p1] + nums[y] == target:
                return [p1, y]

'''
NOW USE HASHMAPS

This TwoSum solution uses O(n) time complexity because we use a single for loop aka. iterate over 
the give array only once. We use the hashmap to store to pair that we are looking for and as
we iterate we constantly check if we have the missing pair in our hashmap
'''
def TwoSum(arr: list, target: int):
    values = {} # empty hashmap to store value
    lenOfArray = len(arr)
    for index in range(lenOfArray):
        currValue = arr[index] #value at that index in the array
        if values.get(currValue) is not None: #check if given key is in the hashmap
            # returns the indexes for the pairs that add up
            return [values[currvalue], index]
        lookingFor = target - currValue #missing pair we are looking for
        #add the lookingFor into dictionary as key and value the index
        values[lookingFor] = index
    return []


'''
CLASSES
    Instance: single set of values of a particular class (ex. it is a specific person). 
        A Person class is a data type with variables for name, age. 
        Valeria is an instance of a Person.
'''     

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayPerson(self):
        print("Name:", self.name, "Age:", self.age)

#create a new person
person1 = Person("Valeria", 21)
person2 = Person("David", 21)

#this displays instance values
person1.displayPerson()
person2.displayPerson()

class StuffedAnimal:
    def __init__(self, name, color, owners):
        self.name = name
        self.color = color
        self.owners = owners
    def displayStuffedAnimal(self):
        print("Name:", self.name, "Color:", self.color, "Owners:", self.owners)
    def canSmoke(self):
        return False

animal1 = StuffedAnimal("Alan", "brown", "David and Valeria")
animal2 = StuffedAnimal("Gizmo", "golden", "David and Valeria")

animal1.displayStuffedAnimal()
animal2.displayStuffedAnimal()

'''
Data Structure: Linked List
Description: Linear connected nodes data structure

Complexity:
    - Search: O(n)
    - Add: O(1)
    - Delete: O(1)

LinkedList:
 - head: Is a Node

Node:
 - data: Value we want to put in
 - next: Pointer to the next node

 Practice Excercise:
 - Delete Node in LinkedList
 - Find Cycle in LinkedList
 - Find Length of Cycle in LinkedList
 - Find the beginning of Cycle in LinkedList
 '''

 