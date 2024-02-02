def add(x,y):
    print(x +y)
def sub(x,y):
    print(x - y)
def multiply(x,y):
    print(x * y)
def divide(x,y):
    if y == 0:
        return ValueError ("divide by zero is called error")
    else:
        print(x / y)
while True :
    num1 = eval(input("enter the number :"))
    num2 = eval(input("enter the sec number:"))
    num = input("operator:")
    if(num == "+"):
        add(num1,num2) 
    elif(num == "-"):
        sub(num1 ,num2) 
    elif(num == "*"):
        multiply(num1 ,num2) 
    elif (num == "/"):
        divide(num1 ,num2) 
    next_calculation = input("Do you want to continue calculation (yes/no): ")
    if next_calculation == "no":
            print("Exiting the calculator")
            break
    else:
        print("invalid number")


    


         

