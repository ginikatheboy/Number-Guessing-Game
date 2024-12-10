def AddNum(x, y):
    print("Performing the addition operation: ")
    return x + y
def SubNum(x, y):
    print("Performing the subtraction operation: ")
    return x - y
def DivNum(x, y):
    print("Performing the division operation: ")
    return x / y 
def MulNum(x, y):
    print("Performing the Multiplication operation: ")
    return x * y 


def Menu():
    print("Menu: ")
    print("For addition operation press 1")
    print("For subtraction operation press 2")
    print("For division operation press 3")
    print("For multiplication operation press 4")
    choice = int(input("Pick an operation: "))
    return choice 

    
def Calculation():
    ch = Menu()

    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a second number: "))

        if ch == 1:
            result = AddNum(num1, num2)
        elif ch == 2:
            result = SubNum(num1, num2)
        elif ch == 3:
            result = DivNum(num1, num2)
        elif ch == 4:
            result = MulNum(num1, num2) 
        else:
            print("Invalid choice! Please enter a valid operation")
            return 
        print(f"The result is: {result}")

    except ZeroDivisionError:
        print("Division by zero is impossible")
    except ValueError:
        print("Please enter valid numbers.")
    

Calculation()
    













