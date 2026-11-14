# # Part 1: Positional and Keyword Arguments (1-10)

# 1. Create a function student_details() that accepts rollno, name, and age and prints all details.
def student_details(roll,name,age):
    print(f"Roll : {roll}  Name : {name}  Age :{age}")
student_details(101,"Payal",22)

# 2. Create a function employee_details() that accepts eid, ename, and salary and returns the employee details.
def employee_details(eid,ename,salary):
    print(f"ID : {eid} Employee_Name : {ename} Salary : {salary}")
employee_details(202,"ABC",50000)

# 3. Create a function addition() that accepts two numbers and returns their addition.
def addition(num1,num2):
    return num1 + num2
print(addition(10,20))

# 4. Create a function student_marks() that accepts a student's name and marks in three subjects and prints total marks.
def student_marks(m1,m2,m3):
    total = m1 + m2 + m3
    return total
n1 = int(input("1st sub marks :"))
n2 = int(input("2nd sub marks :"))
n3 = int(input("3rd sub marks :"))
print(student_marks(n1,n2,n3))

# 5. Create a function product_details() that accepts pid, pname, and price and prints the details
def product_details( pid, pname, price):
    return pid , pname , price
print(product_details(101,"Mobile",25000))


# 6. Create a function rectangle_area() that accepts length and width and returns the area.
def rectangle_area(l,w):
    area = l * w
    return area
print(rectangle_area(15,10))


# 7. Create a function student_info() and call it using positional arguments.
def student_info(roll,name,marks):
    print(f"Roll : {roll} , Name :{name} , Marks :{marks}")
student_info(1,"abc",98)


# 8. Create a function student_info() and call it using keyword arguments in a different order.
def student_info(roll,name,marks):
    print(f"Roll : {roll} , Name :{name} , Marks :{marks}")
student_info(name ="abc", marks = 98,roll = 1)


# 9. Create a function bank_details() that accepts account number, customer name, and balance. Call the function using both positional and keyword arguments separately.
def bank_details(acc_no,name,balance):
    return acc_no , name , balance

s1 =  bank_details(123456,"payal",4000)
s2 =  bank_details(balance = 80000,name="Richa",acc_no = 987654323456)
print("Positional Argument :",s1)
print("Keyword Argument :",s2)


# 10. Create a function calculate() that accepts three numbers and returns their sum, average, maximum,and minimum.
def calculate(num1, num2, num3):
    total = num1 + num2 + num3
    avg = total / 3
    maximum = max(num1, num2, num3)
    minimum = min(num1, num2, num3)

    return total, avg, maximum, minimum

n1 = int(input("1st number: "))
n2 = int(input("2nd number: "))
n3 = int(input("3rd number: "))

result = calculate(n1, n2, n3)

print("Sum:", result[0])
print("Average:", result[1])
print("Maximum:", result[2])
print("Minimum:", result[3])

### Part 2: Default Arguments (11-20)

# 11. Create a function student_details() with city='Pune' as a default argument.
def student_info(roll,name,age,city ="Pune"):
    return roll , name , age , city
print(student_info(101,"abc",18))

# 12. Create a function employee_details() with city='Pune' and company='TKA' as default arguments.
def employee_details(id,name,city="Pune",company="TKA"):
    return id , name , city , company
print(employee_details(201,"Priya"))

# 13.Create a function user_profile() with default values for city and country. Override only one default value while calling the function.
def user_profile(name,city="Pune",country="India"):
    return name ,city , country
print(user_profile("abc",city = "Mumbai"))

# 14. Create a function bank_account() with a default branch name 'Karve Nagar'.
def bank_acc(acc_no,branch = "karveNagar"):
    return acc_no , branch
print(bank_acc("12345678"))

# 15.Create a function course_details() with a default duration of '6 Months'.
def course_details(id,name,duration = 6):
    return f"ID : {id} , Name : {name} , Duration of Course : {duration}"

print(course_details(101,"Python FullStack"))

# 16. Create a function student_details() and call it once without passing the city and once by passing a different city.
def student_details(roll,name,age,city="Pune"):
    print(f"Roll : {roll}  Name : {name}  Age :{age} City : {city}")
student_details(101,"Payal",22)
student_details(102,"Riya",21,city="Mumbai")

# 17. Create a function calculate_bill() that accepts price, quantity=1, and discount=0.
def calculate_bill(price,quantity=1,discount=0):
    print(f"Price : {price} Qty : {quantity} Disc : {discount}")
calculate_bill(10000)
calculate_bill(50000,discount=10)

# 18. Create a function employee_salary() with bonus=5000 as a default argument.
def employee_salary(id,dept,bonus=5000):
    return f"ID : {id} , Dept : {dept} , Bonus : {bonus}"
print(employee_salary(101,"IT"))
print(employee_salary(101,"IT",bonus=6000))

# 19. Create a function movie_details() with language='Hindi' as a default argument.
def movie_details(name,langu = "Hindi"):
    return f"Name : {name} , Language : {langu}"
print(movie_details("Ramayan"))
print(movie_details("Ramayan","Marathi"))

# 20. Create a function user_profile() with default values for city and country. Override only one default value while calling the function.
def user_profile(name,age,city="Pune",country="india"):
    print(f"Name : {name} , Age : {age} ,City : {city} , Country : {country}")

user_profile("Payal",23)
user_profile("Riya",22,"Latur")

### Part 3: return Statement (21-28)

# 21. Create a function that accepts two numbers and returns their addition.
def addition(num1,num2):
    return num1 + num2
print(addition(20,30))

# 22. Create a function that accepts three numbers and returns all three numbers as a tuple.
def numbers(*num):
    return num
print(numbers(10,20,30))
print(type(numbers(10,20,30)))

# 23. Create a function that accepts a student's marks and returns 'Pass' or 'Fail'.
def result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"
n = int(input("enter a number :"))
print(result(n))

# 24. Create a function that accepts a number and returns its square and cube
def squareCube(num):
    n = num ** 2
    n2 = num ** 3
    return n , n2
print(squareCube(3))

# 25. Create a function that accepts two numbers and returns addition, subtraction, multiplication, and division.
def operation(num1,num2):
    return num1+num2 , num1-num2 , num1*num2 , num1/num2
print(operation(30,20))

# 26.Create a function that accepts a string and returns its length.
def lenofstring(s):
    return len(s)
print(lenofstring("python"))

# 27.Create a function that accepts a list of numbers and returns the maximum number.
def maxNumber(list):
    return max(list)

print(maxNumber([98,87,45,100,120,50]))

# 28.Create a function that accepts employee details and returns a formatted string containing all employee information.
def emp_info(id,name,salary):
    return f"ID : {id} , Name : {name} , Salary :{salary}"
print(emp_info(101,"Sanjana",50000))

### Part 4: *args - Variable Number of Arguments (29-36)

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

### Part 5: **kwargs - Keyword Variable Arguments (37-43)

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

##### Part 6: yield and Generator Functions (44-47)

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

### Part 7: Positional-Only Arguments / (48-50)

# 48. Create a function student_info(sid, sname, /) and call it correctly using positional arguments.
def student_info(sid,sname,/):
    return f"ID : {sid} Name : {sname}"
print(student_info(101,"Sanjana"))

# 49. Create a function with rollno, name, and age as positional-only arguments
def info(roll,name,age,/):
    return f"Roll : {roll} Name : {name} ,Age : {age}"
print(info(201,"Suyash",22))

# 50. Create a function addition(num1, num2, /) and perform addition. Try different valid function calls
def addition(num1, num2, /):
    return f"{num1} + {num2} = {num1 + num2}"
print(addition(20,30))


#### Part 8: Keyword-Only Arguments * (51-53)

# 51. Create a function student_info(*, sid, sname) and call it using keyword arguments.
def student(*,sid,sname):
    return f"ID : {sid} Name : {sname}"
print(student(sid=101,sname = "sanjana"))

# 52. Create a function employee_info(*, eid, ename, salary) using keyword-only arguments.
def employee_info(*, eid, ename, salary):
    return f"ID : {eid} ,Name : {ename} ,salary : {salary}"
s = employee_info(eid=101, ename="suyash", salary=50000)
print(s)

# 53. Create a function where name is positional and city and salary are keyword-only arguments.
def info(name,city,salary):
    return f"Name : {name} , City : {city} , Salary : {salary}"
s = info("Sanjana",city="Pune",salary=40000)
print(s)

### Part 9: Global and Local Variables (54-56)

# Create a global variable num1 = 10 and a function containing a local variable num2 = 20. Print their addition inside the function.
num1 = 10
def add():
    num2 = 20
    print(num1 + num2)
add()

# Create a global variable and modify its value inside a function using the global keyword.
num1 = 10
def add():
    global num1
    num1 = 30
    num2 = 20
    print(num1 + num2)
add()

#  Create a program where a local variable and global variable have the same name. Observe and understand their behavior
n1 = 30
def add():
    n1 = 40
    print(n1+n1)
add()
print(n1+n1)

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

### Part 11: Advanced Recursive Function Tasks (61-70)

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