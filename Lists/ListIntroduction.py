'''
Lists are Dynamic in size.
Elements are stored in list with the help of the actual data references. The elemets of list are stored in Contiguous Locations but not Actual Data. 
Advantages :
    1. Random Accessing of elements from list.
    2. Cache Storage.
Disadvantages:
    1. Searching in list is costly when the list is not sorted.
    2. Inserting and deleting a specific element has also has the linear time complexity.
'''

# Some Basic List Functions

'''

lst = [10, 20, 30, 40, 50]

lst.append(60) # inserts 60 at the end of the list

print(20 in lst) # checks whether 20 is present in list or not. Returns True if present, Returns False Otherwise.

lst.insert(1, 15) # Inserts 15 at index 1

print(lst)

print(lst.index(15)) #Returns the index value of an element.

'''

# Some Basic Problems on Lists

'''
# Printing the elements in a list smaller than a specific element.

lst = list(map(int, input().split()))
target = int(input())

def smallestElements(lst, target):
    return list(filter(lambda x : x if x < target else None, lst))
    
print(smallestElements(lst, target))

'''


# Seperating even and odd numbers from a list of numbers

def segregate(lst):
    even = list(filter(lambda x:x if x%2==0 else None, lst))
    odd = list(filter(lambda x:x if x%2!=0 else None, lst))
    return even, odd
even, odd = segregate(lst)

print(even, odd)












