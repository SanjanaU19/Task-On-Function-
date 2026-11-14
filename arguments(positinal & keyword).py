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

