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