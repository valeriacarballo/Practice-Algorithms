'''
return distinct values from a list including duplicates
    Given {1, 2, 6, 6, 6, 10, 14, 14}; return -> {1, 2, 6, 10, 14}
'''
numsToReturn = []
def distinctValues(nums: list):
    for i in nums:
        if i in numsToReturn:
            continue
        numsToReturn.append(i)
    return numsToReturn





'''
Write a function that reverses a string.

Example:
Input: "hello"
Output: "olleh"
'''
# using for loop
def reverseString (string: str):
    revStr = ""
    for i in string:
        revStr = i + revStr
    return revStr





'''
Write a function that takes in two strings and returns true if the second string is substring of the first, and false otherwise.

Examples: 
Input: laboratory, rat
Output: true

Input: cat, meow
Output: false
'''
def findSubstring (string:str, substring: str):
    if substring in string:
        return True
    else:
        return False

#print(findSubstring("laboratory", "rat"))




'''
Given a prime number, return the next smallest prime number

Examples:
Input: 3
Output: 5
'''
def getPrime (number: int):
    nextPrime = number + 2
    return nextPrime





def fizzbuzz (nums: list):
    for i in nums:
        if i%3==0 and i%5==0:
            print("fizzbuzz")
            continue
        if i%3==0:
            print("fizz")
            continue
        if i%5==0:
            print("buzz")
            continue
        else:
            print(i)
       


def fibbonaci(n:int):
    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i in range(1,91):
        ic1 = len(fib) - 1
        ic2 = len(fib) - 2
        x = fib[ic1] + fib[ic2]
        fib.append(x)
    return fib[n]





'''
Given an array of size n and a number x, determine the first two elements in the array, if any, whose sum is exactly x. Return indices.
'''

values = {}
def TwoSum(arr: list, target: int):
    lenOfArr = len(arr)
    for index in range(lenOfArr):
        currValue = arr[index]
        if values.get(currValue) is not None:
            return [values[currValue], index]
        lookingFor = target - currValue
        values[lookingFor] = index


'''
Find the element that appears k number of times in an array
input: [8, 7, 9, 6, 7, 5, 1], k = 2
output: 7

assumption: if there are more than one number that appears k times, return the first number (easiest option)
            if no number appears k time, return None

if key exists, increment value by 1
{
    8: 1
    7: 2
    9: 1
    6: 1
    5: 1
    1: 1

}

input: [8, 7, 9, 6, 7, 5, 1, 7]
'''

def frequent_num (arr: list, k: int):
    if len(arr) == 0:
        return []

    # populating the dictionary
    d = {}
    for num in arr:
        curr_val = d.get(num)

        if curr_val != None:
            #add 1 to the value
            d[num] = d[num] + 1
            continue

        # setting num as key and value as 1 into the dict
        d.setdefault(num, 1)

    nums_k_times = []
    for num in arr:
        curr_val = d.get(num)
        if curr_val == k:
            nums_k_times.append(num)
            
    return nums_k_times


    


        
