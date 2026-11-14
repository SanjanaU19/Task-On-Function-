# 29. Create a function using *args to accept any number of integers and return them as a tuple.
def numbers(*num):
    return num
print(numbers(1,2,3,4,5,6))

# 30. Create a function using *args to calculate the sum of any number of values.
def numbers(*num):
    total = 0
    for i in num:
        total += i
    return total
print(numbers(1,2,3,4,5,6))

# 31. Create a function using *args to find the maximum number
def maxi(*num):
    return max(num)
print(maxi(98,56,39,45,91,54))

# 32. Create a function using *args to find the minimum number.
def find_min(*num):
    return min(num)
print(min(98,56,39,45,91,54))

# 33. Create a function using *args to calculate the average of all numbers.
def avg_num(*num):
    return sum(num) / len(num)
print(avg_num(10,20,30,25,15,22))

# 34.Create a function using *args to print all student names passed to the function.
def names(*n):
    return n 
print(names("Sanjana","Suyash","Neha","Shweta"))

# 35.Create a function using *args that counts how many values are passed to the function.
def values(*num):
    count = 0
    for i in num:
        count += 1
    return count
print(values(1,2,3,4,5,6,7,8))

# 36.Create a function using *args that returns all even numbers from the given arguments.
def even(*num):
    res = []
    for i in num:
        if i % 2 == 0:
            res.append(i)
    return res
print(even(5,10,15,20,25,30,21,32))

