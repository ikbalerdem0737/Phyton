print("---Calculator---")
print("1.Addition\n2.Substraction\n3.Multiplication/n4.Division")
operation=input("Choose an operation(1-4):")
first_number=int(input("Enter first number:"))
second_number=int(input("Enter second number:"))
f=first_number
s=second_number
if operation=="1":
    print("result:",f+s)
elif operation=="2":
    print("result:",f-s)
elif operation=="3":
    print("result:",f*s)
elif operation=="4":
    if s==0:
        print("you can not divide by zero")
    else:
        print("result:",f/s)
else:
    print("Entered invalid operation please enter valid operations")
