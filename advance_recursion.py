### Part 11: Advanced Recursive Function Tasks (61-70)

# 61. Create a recursive function to check whether a given string is a palindrome or not. Example: 'madam'-> Palindrome.
def palindrome(s1):
    reverse = ""
    for char in s1:
        reverse = char + reverse

    if s1 == reverse:
        return "Palindrome"
    else:
        return "NOt a Palindrome"

print(palindrome("madam"))

# 62. Create a recursive function to calculate the factorial of a given number. Example: 5! = 120.
def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)
print(fact(5))

# 63. Create a recursive function to print or generate the Fibonacci series up to n terms.
def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num -1) + fibo(num - 2)
print(fibo(5))

def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a, b = b, a+b
fibo(7)

# 64. Create a recursive function to reverse a given string. Example: 'Python' -> 'nohtyP'.
def reverse_word(s1):
    reverse = ""
    for char in s1:
        reverse = char + reverse 
    return reverse
print(reverse_word("Python"))

# 65. Create a recursive function to calculate the sum of digits of a number. Example: 12345 -> 15.
def add(num):
    if num == 0:
        return 0
    d = num % 10
    return d + add(num // 10)
print(add(12345))

# 66. Create a recursive function to calculate the power of a number. Example: 2 raised to power 5 -> 32.
def power(num,p):
    if p == 0:
        return 1 
    return num * power(num , p-1)
print(power(2,5))

# 67. Create a recursive function to count the total number of digits in a given number. Example: 123456 -> 6
def count_num(num):
    if num == 0:
        return 0
    d = num % 10
    num = num // 10
    count = 1
    return count + count_num(num)
print(count_num(1234567))

# 68. Create a recursive function to find the Greatest Common Divisor (GCD) of two numbers. Example: 12 and 18 -> 6.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(12, 18))

# 69. Create a recursive function to calculate the product of numbers from 1 to n.
def product(n):
    if n == 1:
        return 1
    return n * product(n-1)
print(product(4))

# 70. Create a recursive function to count the total number of vowels in a given string. Example: 'Education'-> 5.
def vowels(s):
    if s == "":
        return 0
    count = 0
    if s[0] in "AEIOUaeiou":
        count = 1
    return count + vowels(s[1:])
print(vowels("Python"))