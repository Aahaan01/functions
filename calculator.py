a=int(input("Please enter a number: "))
b=int(input("Please enter your second number: "))
operation=str(input("Please enter the function: add or sub or mul or div: "))
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
if operation=="add":
    print("Sum of two numbers is:", add(a,b))
elif operation=="sub":
    print("Difference of two numbers is:", sub(a,b))
elif operation=="mul":
    print("Product of two numbers is:", mul(a,b))
elif operation=="div":
    print("Quotient of two numbers is:", div(a,b))
else:
    print("Operation is invalid.")
