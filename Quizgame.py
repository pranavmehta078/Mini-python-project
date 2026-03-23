#This is for Quiz game program

score = 0

print("Welcome to the Quiz")

#Question 1
print("What is the 2 + 2?")
ans =int(input("The answer is "))

#check condition for answer
if ans == 4 :
    print("This is the right answer")
    score = score + 1
    print("Your score is:", score)
else:
    print("This is the Wrong Answer")

#Question 2
print("What is the capital of india?")
ans = input("The answer is :")

# check condition for answer
if ans.lower() == "delhi":
    print("This is the right answer")
    score = score + 1
else:
    print("This is the Wrong Answer")

print("Your score is:", score)