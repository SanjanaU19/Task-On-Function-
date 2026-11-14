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