while True:
    print("\n===== Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Option chuno: ")

    if choice == "5":
        print("Calculator band ho gaya.")
        break

    a = int(input("Pehla number: "))
    b = int(input("Dusra number: "))

    if choice == "1":
        print("Answer =", a + b)

    elif choice == "2":
        print("Answer =", a - b)

    elif choice == "3":
        print("Answer =", a * b)

    elif choice == "4":
        if b == 0:
            print("0 se divide nahi kar sakte.")
        else:
            print("Answer =", a / b)

    else:
        print("Galat option!")
