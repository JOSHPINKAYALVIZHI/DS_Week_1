num_1=int(input ("Enter number_1 :"))
num_2=int(input ("Enter number_2 :"))
print("1.[+]")
print("2.[-]")
print("3.[*]")
print("4.[/]")
operation=int(input("Enter the operation to done :"))
def switch(operation):
    if operation == 1:
        print(num_1 ," + ",num_2 ," : " , num_1+num_2)
    elif operation == 2:
        print(num_1 ," - ",num_2 ," : " , num_1-num_2)
    elif operation == 3:
        print(num_1 ," * ",num_2 ," : " , num_1*num_2)
    elif operation == 4:
       if num_2 != 0:
            print(num_1, "/", num_2, ":", num_1 / num_2)
       else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid operation..!!")
        
switch(operation)

