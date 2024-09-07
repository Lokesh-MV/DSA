'''
Comprehension : Comprehensions in Python gives an easy syntax to create an iterable element from an iterable. 

Eg : Getting list of even numbers from a list of numbers --> res = list(x for x in range(11) if x%2==0)

'''

# Problems on Comprehension

'''

#Returning a list of elements that are smaller than target value from a list

lst = list(map(int, input().split()))
target = int(input())

def smallElements(lst, target):
    return list(x for x in lst if x < target)
    
print(smallElements(lst, target))
    
'''

'''

# Returning the vowels present in a string

str = 'Nothing is Complicated'

res = list(x for x in str if x in 'aeiou')

print(res)

'''

'''

# Storing the count of each character in a string

str = 'Nothing is Complicated'

res = {x : str.count(x) for x in str}

print(res)

'''

'''

# Returning the count of each vowel present in a string

str = 'Nothing is more complicated'

res = {x : str.count(x) for x in str if x in 'aeiou'}

print(res)

'''

'''

# Finding the second largest element in a list

nums = list(map(int, input().split()))

largest = nums[0]
sl = None
for i in range(1, len(nums)):
    if nums[i] > largest:
        sl = largest
        largest = nums[i]
    elif nums[i] != largest:
        if sl == None or nums[i] > sl:
            sl = nums[i]
        
print(sl, largest)
'''

'''
nums = list(map(int, input().split()))

def checkSorted(nums):
    largest = nums[0]
    for i in range(1, len(nums)):
        if nums[i] <= largest:
            return False
            break
        elif nums[i] < nums[i-1]:
            return False
            break 
    return True

print(checkSorted(nums))

'''
'''
nums = list(map(int, input().split()))  

def checkSorted(nums):
    i = 1
    while i < len(nums):
        if nums[i-1] > nums[i]:
            return False
        i += 1
    return True

print(checkSorted(nums))    

'''

# sort() : modifies the given list and where as the sorted() creates a new list. Eg : l.sort() and sorted(l)



        
            



