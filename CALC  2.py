while not False:
    print("Options: ")
    print("Enter '+' to add")
    print("Enter '-' to subract")
    print("Enter '*' to multiply")
    print("Enter '/' to divide")
    print("Enter '%' for modulo")
    print("Enter '^' for square")
    print("Enter 'Q' to stop the operation and quit the program")
    choice =  input("Choose an option: ")
    if choice == "Q":
        print("Thank you, goodbye")
        break
    elif choice == ("+"):
        a = float(input("Enter the first number: "))
        b = float(input("Enter another number: "))
        result = a + b
        print("Your answer in adding the two numbers is", result)
    elif choice == ("-"):
        a = float(input("Enter the first number: "))
        b = float(input("Enter another number: "))
        result = a - b
        print("Your answer in subtacting the two numbers is", result)
    elif choice == ("/"):
        a = float(input("Enter the first number: "))
        b = float(input("Enter another number: "))
        result = a // b
        print("Your answer in deviding the two numbers is", result)
    elif choice == ("*"):
        a = float(input("Enter the first number: "))
        b = float(input("Enter another number: "))
        result = a * b
        print("Your answer in multiplying the two numbers is", result)
    elif choice == "%":
        a = float(input("Enter the first number: "))
        b = float(input("Enter another number: "))
        result = a % b
        print("The remainder in dividing" , a, "by", b, "is", result)
    elif choice == "^":
        a = float(input("Enter the number: "))
        #b = float(input("Enter another number: "))
        result = a **2
        print("Your answer in finding the square of ", a, "is", result)
    else:
        print("Invalid character, choose from the given options only")
        print("Good luck")
