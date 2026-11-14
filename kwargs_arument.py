# 37. Create a function using **kwargs to accept student details and return them as a dictionary.
def student_details(**n):
    return n 
print(student_details(roll=101, name="sanjana", age=22))

# 38. Create a function using **kwargs to accept employee information such as eid, ename, salary, and city.
def emp_details(**n):
    return n 
s = emp_details(eid = 101,ename="Riya",salary=50000,city="Pune")
print(s)

# 39. Create a function using **kwargs to print all key-value pairs.
def student(**s):
    return s
s1 = student(id = 101 , name = "Sanjana",age = 22)
print(s1)

# 40. Create a function using **kwargs to accept product details
def product_details(**p):
    return p
p1 = product_details(pid = 201,pname = "mobile",price = 40000 , qty = 5)
print(p1)

# 41. Create a function using **kwargs to accept bank customer details
def customer_details(**n):
    return n
n1 = customer_details(acc_no = 1234567654 , acc_name = "Sanjana",amount = 5000)
print(n1)

# 42. Create a function that prints 'Task Started', returns the **kwargs dictionary, and observe whether the code after return executes.
def task(**kwargs):
    print("Task Started")
    return kwargs
    print("Task Completed")
result = task(name="Sanjana", age=22, city="Pune")
print(result)

# 43. Create a function using **kwargs and count the total number of key-value pairs received.
def count_items(**num):
    count = len(num)
    return count
res = count_items(name = "sanjan",age=22,city="pune",marks=98)
print(res)