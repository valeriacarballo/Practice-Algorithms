'''
1. Write a function to remove duplicates from the array
input: [1, 5, 6, 3, 2, 2, 2, 5, 3]
output: [1, 5, 6, 3, 2]
'''

'''
Submission comments:
    - You let the method .fromKeys() do all the heavy lifting, no bueno
    - Clever way of solving the problem, but not algorithmically correct

Question Grade: C+

def removeDups(arr: list):
    #convert list into hashmap keys (hashmaps cannot have repeating keys)
    dictionary = dict.fromkeys(arr)
    #convert hashmap back into list
    newList = list(dictionary)
    print(newList)

'''

def removeDups (arr: list):
    tmp = arr 
    newArr = []
    for i in tmp:
        if i in newArr:
            continue
        newArr.append(i)
    print(newArr)

'''

2. Implement an algorithm to reverse an array in linear time
input: [10, 8, 2]
output: [2, 8, 10] 
'''

'''
Submission comments:
    - Using extra space, could be better using 2 pointer algorithm
    - Mutating variables, not good
    - Hidden mutation when .pop(), very bad
    - No helper method, good
Question Grade: B+

newArr = []
def reverseArr(arr: list):
    for i in range(len(arr)):
        i = len(arr) - 1 # Mutating i, not a good idea 
        x = arr.pop(i) # Hidden mutation, very bad
        newArr.append(x)
    print(newArr)
'''
def reverseArr(arr: list):
    tmp = arr
    for i in range(len(tmp)):
        for j in range(len(tmp)):
            y = len(tmp) - 1
            if i == y:
                return
            
            
            
