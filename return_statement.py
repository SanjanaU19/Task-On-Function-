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