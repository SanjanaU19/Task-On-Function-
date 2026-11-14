# 44. Create a generator function that accepts student details using **kwargs and yields the dictionary.
def student_details(**kwargs):
    yield kwargs
result = student_details(name="Sanjana", age=22, marks=90)
print(next(result))

# 45. Create a generator function that yields numbers from 1 to 10.
def numbers(**num):
    for i in range(1,11):
        yield i
res = numbers()
for i in res:
    print(i)

# 46. Create a generator function that accepts a number n and yields numbers from 1 to n.
def numbers(n):
    for i in range(1,n+1):
        yield i
res = numbers(6)
for i in res:
    print(i)

# 47. Create a generator function that accepts multiple numbers using *args and yields each number one by one.
def numbers(*num):
    for i in num:
        yield i
s = numbers(10,20,30,40,50)
for i in s:
    print(i)

# 48. Create a generator function that accepts multiple numbers using *args and yields only even numbers.
def numbers(*num):
    for i in num:
        if i % 2 == 0:
            yield i
s = numbers(32,54,76,77,33,44,21)
for i in s:
    print(i)