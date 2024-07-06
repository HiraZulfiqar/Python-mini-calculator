print("Welcome to the mini calculator!")

num1 = float(input("Enter your fist number here: "))
num2 = float(input("Enter your second number here: "))

print("press 1 for Addition \n press 2 for Subtraction \n press 3 for Multiplication \n press 4 for Division")
choice = int(input("enter your choice from 1-4: "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 /  num2)

else:
      print("you enter invalid input")
