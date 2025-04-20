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

def modulus(num_1, num_2):
    return num_1 % num_2

def exponentiate(num_1, num_2):
    return num_1 ** num_2

def floor_divide(num_1, num_2):
    if num_2 != 0:
        return num_1 // num_2
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
        print("5. [%] Modulus")
        print("6. [**] Exponentiation")
        print("7. [//] Floor Division")
        
        operation = int(input("Enter the operation number (1/2/3/4/5/6/7): "))
        
        
        operations = {
            1: add,
            2: subtract,
            3: multiply,
            4: divide,
            5: modulus,
            6: exponentiate,
            7: floor_divide
        }

        if operation in operations:
            result = operations[operation](num_1, num_2)
            print(f"Result: {result}")
        else:
            print("Invalid operation. Please select a valid operation number (1-7).")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    
    finally:
        print("\nCalculator operation has finished.")  
calculator()
