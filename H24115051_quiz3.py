print("Welcome to simple calculator program")
while True:
   while True:
       try:
           print("Welcome to the simple calculator program!")
           first = input(float("Enter the first number :"))
           second = input(float("Enter the second number:"))
           break
       except ValueError:
            print("Numbers only")
   opt = input("Select an arithmetic operation (+, -, *, /):")
        if opt == "+":
            plus = first + second
            print(plus)
        if opt == "-":
            min = first - second
            print(min)
        if opt == "*":
            times = first * second
            print(times)
        if opt == "/":
            div = first / second
            print(div)
        choice = input ("do you want to try again:")
        if choice == "no":
            print("goodbye")
            break
        if choice == "yes":
            continue





