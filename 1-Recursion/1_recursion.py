# Factorial with recursion

def factorial(n):
    if(isinstance(n,float) or n < 0):
        return print('Please use positive number to find factorials!')
    if n == 0 or n == 1:
        return 1;
    else:
        return n * factorial(n-1);

# print(factorial(7));

# Find Fibonacci numbers with recursion

def fibonacci(n):
    if(isinstance(n,float) or n < 0):
        return print('Please use positive number only.');
    if(n == 1 or n == 0):
        return n;
    return fibonacci(n-1) + fibonacci(n-2);

# print(fibonacci(8));

# Sum of Digits

def sumOfDigits(n):
    if n == 0:
        return 0;
    else:
        return int(n%10) + sumOfDigits(int(n/10));

# print(sumOfDigits(65));

# Power of a number

def power(x,n):
    if x < 0 or isinstance(x,float) or n < 0 or isinstance(n,float):
        return print('Please enter positive numbers only');
    elif n == 0:
        return 1;
    elif n == 1:
        return x;
    else:
        return x * power(x,n-1);        

# print(power(6,4));

# Greatest Common Divisor of 2 numbers

def greatestCommonDivisor(a,b):
    if a < 0:
        a = a * -1;
    elif b < 0:
        b = b * -1;
    elif b == 0:
        return a;
    else:
        return greatestCommonDivisor(b, a%b);

# print(greatestCommonDivisor(48,18));

# Decimal to Binary

def decimalToBinary(n):
    if isinstance(n,float):
        print('Parameter must be a positive number');
    elif n == 0:
        return 0;
    else:
        return n%2 + 10 * decimalToBinary(int(n/2));

# print(decimalToBinary(10));

    