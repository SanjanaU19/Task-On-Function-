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
