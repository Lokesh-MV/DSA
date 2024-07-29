#  Counting the number of digits in a number

def countDigits(n):
    count = 0
    while n!=0:
        n=n//10
        count+=1
    return count

def palindrome(n):
    rev = 0
    temp = n
    while temp!=0:
        lastDigit = temp%10
        rev = rev*10 + lastDigit
        temp = temp//10
    if rev == n:
        return True
    else:
        return False
    
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    return (a*b)/gcd(a,b)


if __name__ == '__main__':
    # num = int(input("Enter the number to count digits : "))
    # print('The number of digits in number are : %i'%countDigits(num))

    # num = int(input("Enter the number to check for palindrome : "))
    # print(palindrome(num))

    a, b = map(int, input("Enter the numbers :").split())
    print(lcm(a,b))
