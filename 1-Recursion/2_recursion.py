# Power of a number

def power(base,exponent):
    if exponent == 0:
        return 1;
    return base * power(base, exponent-1);

# print(power(5,1));

# Factorial of a number

def factorial(n):
    if n <= 1:
        return 1;
    return n * factorial(n-1);

# print(factorial(10))

# Product of array

def productOfArray(arr):
    if len(arr) == 0:
        return 1;
    return arr.pop(-1) * productOfArray(arr);

# print(productOfArray([1,2,3]))

# Recursive range

def recursiveRange(n):
    if n <= 0:
        return 0;
    return n + recursiveRange(n-1);

# print(recursiveRange(10));

# Reverse string

def reverse(s):
    if len(s) == 1:
        return s[-1];
    return s[-1] + reverse(s[0:-1]);

# print(reverse('appmillers'));

# Palindrome

def isPalindrome(s):
    return s[0:] == s[::-1]

# print(isPalindrome('tacocat'))

# somerecursive with array and callback

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True;

# print(someRecursive([1,2,3,4], isOdd))

# Captalize first letter of word

def capitaliseFirst(arr):
    b = [];
    if len(arr) == 0:
        return b;
    b.append(arr[0][0].upper() + arr[0][1:]);
    return b + capitaliseFirst(arr[1:]);

# print(capitaliseFirst(['cat', 'pig', 'fox']));

# Capitalise Words

def capitaliseWords(arr):
    b = [];
    if len(arr) == 0:
        return b;
    b.append(arr[0].upper());
    return b + capitaliseWords(arr[1:]);

print(capitaliseWords(['i', 'am', 'learning', 'recursion']));

