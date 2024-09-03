# Lists are Dynamic. 
# and in place of elements, references of actual data are stored which are contiguous and actual data may not be Contiguous.
# Random Access and Cache Storage are advantages with lists.
# Search in list when the list is not sorted, Inserting and deleting a specific element is costly and these are the de-merits with Lists in Python.

# lst = [10, 20, 30, 40, 50]

# lst.append(60) # inserts 60 at the end of the list

# print(lst)

# print(20 in lst) # checks whether 20 is present in list or not. Returns True if present, Returns False Otherwise.

# lst.insert(1, 15) # Inserts 15 at index 1

# print(lst)

# print(lst.index(15)) #Returns the index value of an element.

lst = list(map(int, input().split()))
target = int(input())

# Seperating the elements even and odd

# def segregate(lst):
#     even = list(filter(lambda x:x if x%2==0 else None, lst))
#     odd = list(filter(lambda x:x if x%2!=0 else None, lst))
#     return even, odd
# even, odd = segregate(lst)

# print(even, odd)

def smallestElements(lst, target):
    return list(filter(lambda x : x if x < target else None, lst))

print(smallestElements(lst, target))


