print("Simple Calulator")
num1= float(input("Enter first number:"))
num2= float(input("Enter second number:"))

def calculate(num1,num2):
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    
    select= int(input("Enter Operation number(1-4):"))
    
    if select== 1:
        print("Sum is:",num1 + num2)
    elif select== 2:
        print("Difference is:",num1 - num2)
    elif select== 3:
        print("Product is:",num1 * num2)
    elif select== 4:
        if num2 != 0:
            print("Quotient is:",num1 / num2)
        else:
            print("Error! Division by zero is not allowed")
    else:
        print("Invalid operation number.Please enter number between 1 and 4:")
        
calc=calculate(num1,num2)
print(calc)