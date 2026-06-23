operator = input("enter an operator (+ , _ , * , / ) : ")
num1 = float(input("enter 1st number : "))
num2 = float(input("enter @nd number : "))

if operator == "+":
    result = num1 + num2 
    print(round(result , 3))

elif operator == "-":
    result = num1 - num2 
    print(round(result , 3))
    
elif operator == "*":
    result = num1 * num2 
    print(round(result , 3))

elif operator == "/":
    result = num1 / num2 
    print(round(result , 3))
    
else:
    print(f"{operator} is not a valid operator ")