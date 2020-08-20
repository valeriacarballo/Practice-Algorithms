'''
create a function that takes two or more arrays 
and returns an array of the symmetric difference (set of elements which 
are in either of the two sets but not in both) of the provided arrays

'''
#for just two arrays
def symmetricDifference(arr1: list, arr2: list):
    diff = []
    for i in arr1:
        if i in arr2:
            continue
        diff.append(i)
    for i in arr2:
        if i in arr1:
            continue
        diff.append(i)
    return diff
        
def symmetricDifference2(*argv):
    diff: dict = {}
    for index in range(len(argv)):
        print(index)
        for num in argv[index]:
            if diff.get(num) is None:
                diff[num] = False
                continue
            else:
                diff[num] = True
    diffArr: list = []
    for key in diff.keys():
        if diff[key] == True:
            continue
        else:
            diffArr.append(key)
    return diffArr


a = [1, 4, 7]
b = [1, 3, 4]
c = [1, 8]

#print(symmetricDifference2(a, b, c))


'''
compare and update the inventory stored in a 2D array against a second
2D array of a fresh delivery. Update the current existing inventory item
quantities in the first array. If an item cannot be found, add new item
and quantity into the inventory array. The returned inventory array
should be in alphabetical order.
'''
# 2D array ex. = [[1,2], [6, 7], [9,3]]

# complexity : n + k
def updateInventory(inventory: [int, str], newFruits: [int, str]):
    fruitsdict: dict = {} # empty hashmap
    for i in newFruits:
        inventory.append(i) # add the new fruits to the inventory

    for j in inventory:
        if fruitsdict.get(j[1]) is not None: # checks if key exists in fruitsdict
            fruitCount: int = j[0] # original number of fruit
            fruitName: str = j[1]
            currFruitCount: int = fruitsdict[fruitName]
            fruitsdict[fruitName] = currFruitCount + fruitCount
        else:
            fruitsdict[j[1]] = j[0]
    return fruitsdict

inventory = [[21, "apples"], [7, "peaches"], [8, "oranges"]]
newFruits = [[3, "peaches"], [1, "oranges"]]

#print(updateInventory(inventory, newFruits))

arr = [4, 2, 3, 6]

def maxDifference(arr: list):
    for p1 in range(len(arr)):
        p2 = p1 + 1
        if p2 >= len(arr):
            break
        if arr[p1] > arr[p2]:
            continue
        if arr[p2] > arr [p1]:
            diff = arr[p2] - arr[p1]
        return diff
        if diff == None:
            return None


print(maxDifference(arr))