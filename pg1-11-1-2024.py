# write a program to print the given odd or even.
user_input=int(input("Enter the number :"))
if user_input % 2 == 0:
    print("The given number is even.")
elif user_input % 2 != 0:
    print("The given number is odd.")
elif user_input == 0:
    print("The given number is zero")