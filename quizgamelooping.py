# Using While loop

while True:
    start = input("Do you want to start a Quiz? (Yes / No): ").lower()

    if start == "no":
        print("Good Bye")
        break   # stops the loop

    elif start == "yes":

        score = 0

        # Question 1
        print("\nQ1: What is 2 + 2?")
        if input("Answer: ") == "4":
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

        # Question 2
        print("\nQ2: Capital of India?")
        if input("Answer: ").lower() == "delhi":
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

        print("\nFinal Score:", score)

    else:
        print("Invalid input, please type Yes or No.")