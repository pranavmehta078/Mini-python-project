#this project will analy the number 

#intialize the varible with 0
total = 0
count = 0

#Loop Execute
while True:

    #Take input from user as number or q
    Userinput = input("Enter the number OR q for quit :")

    #Check If user input id q
    if Userinput == "q":
        print("Exit")
        break
    #If user input any number 
    number = int(Userinput)
    total = total + number
    count += 1
    
    #Check if any number no enter the count or if number enter the what count 
    if count == 0:
        print("No numbers entered")
    
    else:
        print("Total:", total)
        print("Average:", total / count)
