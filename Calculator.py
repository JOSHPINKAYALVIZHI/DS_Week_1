def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    if num_2 != 0:
        return num_1 / num_2
    else:
        return "Division by zero is not allowed."

def calculator():
    try:
        num_1 = int(input("Enter number 1: "))
        num_2 = int(input("Enter number 2: "))
        
        print("Select operation:")
        print("1. [+] Addition")
        print("2. [-] Subtraction")
        print("3. [*] Multiplication")
        print("4. [/] Division")
        
        operation = int(input("Enter the operation number (1/2/3/4): "))
        
        if operation == 1:
            print(f"{num_1} + {num_2} = {add(num_1, num_2)}")
        elif operation == 2:
            print(f"{num_1} - {num_2} = {subtract(num_1, num_2)}")
        elif operation == 3:
            print(f"{num_1} * {num_2} = {multiply(num_1, num_2)}")
        elif operation == 4:
            print(f"{num_1} / {num_2} = {divide(num_1, num_2)}")
        else:
            print("Invalid operation. Please select 1, 2, 3, or 4.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    
    finally:
        print("\nCalculator operation has finished.")  
calculator()


