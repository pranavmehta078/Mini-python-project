# Initial Balance Define
Initialamount = 10000

# Define the Options
print("Welcome to ATM")
print("1. Check Balance")
print("2. Cash Withdraw")
print("3. Cash Deposit")

choice = int(input("Please Select the option: "))

if choice == 1:
    print("Your Account Balance is", Initialamount)

elif choice == 2:
    enteramount = float(input("Please enter amount to withdraw: "))
    if enteramount > Initialamount:
        print("Insufficient Balance")
    else:
        remainamount = Initialamount - enteramount
        print("Your Remaining balance is", remainamount)

elif choice == 3:
    enteramount = float(input("Please enter amount to Deposit: "))
    totalamount = Initialamount + enteramount
    print("Your Updated balance is", totalamount)

else:
    print("Invalid Input")