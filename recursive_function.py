# Part 10: Recursive Functions (57-60)

# 57. Create a recursive function to print numbers from 10 to 1.
def numbers(n):
    if n == 0:
        return 
    print(n)
    numbers(n-1)
numbers(10)

# 58. Create a recursive function to print numbers from 1 to 10.
def numbers(n):
    if n == 0:
        return 
    numbers(n-1)
    print(n)    
numbers(10)

# 59. Create a recursive function to calculate the sum of the first n natural numbers.
def sum1(n):
    sum = 0
    if n == 0:
        return 0
    return n + sum1(n-1)
print(sum1(10))

# 60. Create a recursive function to calculate the factorial of a number
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(6))