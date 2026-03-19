#In this project we enter the inout from user and according to selection of the operator calculation perform

num1 = int(input("Please Enter number 1 :"))
num2 =int(input("please enter number 2:")) 

#Select the operator to perform
operation = input("Select the operator +, -,/, * :")

if operation == "+":
    Result = num1 + num2
    print("Sum of the two number is :",Result)
elif operation == "-":
    Result = num1 - num2
    print("Sub of the two number is :",Result)

elif operation == "-":
    Result = num1 / num2
    print("Div of the two number is :",Result)

elif operation == "*":
    Result = num1 * num2
    print("Mul of the two number is :",Result)

else :
    print("Invalid input")