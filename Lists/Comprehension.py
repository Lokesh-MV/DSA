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
