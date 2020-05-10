'''
Exam 1
Name: Valeria Carballo (aka tiny)
Data: 04/01/2020
'''
'''
1. Write a function to remove duplicates from the array
input: [1, 5, 6, 3, 2, 2, 2, 5, 3]
output: [1, 5, 6, 3, 2]
'''

def removeDups(arr: list):
    #convert list into hashmap keys (hashmaps cannot have repeating keys)
    dictionary = dict.fromkeys(arr)
    #convert hashmap back into list
    newList = list(dictionary)
    print(newList)

'''
2. Implement an algorithm to reverse an array in linear time
input: [10, 8, 2]
output: [2, 8, 10] 
'''
newArr = []
def reverseArr(arr: list):
    for i in range(len(arr)):
        i = len(arr) - 1
        x = arr.pop(i)
        newArr.append(x)
    print(newArr)


'''
3. Write an algorithm to determine if a given string is a palindrome
input: "racecar"
output: True

input: "love you"
output: False
'''

def listToStr(arr: list):
    strl = ""
    return strl.join(arr)

def isPalindrom(word: str):
    arr = list(word)
    revArr = []

    for i in range(len(arr)):
        i = len(arr) - 1
        x = arr.pop(i)
        revArr.append(x)
    print(listToStr(revArr))

    if listToStr(revArr) == word:
        print(True)
    else:
        print(False)

'''
4. Implement an algorithm to detect if a linked list contains a cycle. 
Return False if no cycle is found, otherwise True if cycle is found.



Input: A node representing the head of the linkedlist
Please use the below template to implement your solution
class Solution:
    def hasCycle(self, head) -> boolean:
        # Implement your logic here

''' 

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addNode(self, node):
        if self.head == None:
            self.head = node
            return
        
        curr = self.head

        while curr.next != None:
            curr = curr.next 
        
        curr.next = node
        return

    def printList(self):
        if self.head == None:
            return
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next
    
    def hasCycle(self, head):
        if self.head == None:
            print(False)
        
        p1 = self.head
        p2 = p1.next

        while p2 != None:
            if p2.next == None:
                print(False)
                break
            else:
                p2 = p2.next.next
                p1 = p1.next
                if p1 == p2:
                    print(True)
                    break
               


#test

website_history = LinkedList()

node_1 = Node("google.com", None)
node_2 = Node("google.com/search", None)
node_3 = Node("google.com/search/hilary", None)
node_4 = Node("google.come/search/hilary/boobs", node_2)

website_history.addNode(node_1)
website_history.addNode(node_2)
website_history.addNode(node_3)
website_history.addNode(node_4)


website_history.hasCycle(node_1)

'''
5. True/False: Arrays & linkedlist are index based
Answer: False

6. True/False: Search in hashmap is O(n)
Answer: False

7. True/False: Array's can insert in O(n) while LinkedList insert in O(logn)
Answer: False

8. True/False: Binary Search has complexity O(n)
Answer: False

9. True/False: A LinkedList is connected by linking together nodes that point to other nodes
Answer: True

10. True/False: In a Class, the constructor is the initial configuration for that class. The constructor is optional and does not need any parameters by default.
Answer: True
'''