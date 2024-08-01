def calculator(a, b):
    cal = input('''What do you want to do?
                 Addition: +
                 Subtraction: -
                 Multiplication: *
                 Division: /
                 Enter your choice: ''')
    if cal == "+":
        print(a+b)
    elif cal == "-":
        print(a-b)
    elif cal == "*":
        print(a*b)
    else:
        print(a//b)
        
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(calculator(a, b))
