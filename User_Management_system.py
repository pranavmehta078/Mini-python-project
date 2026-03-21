#We are building a simple system that:

# Takes multiple users

# Stores their details

# Shows menu again & again (loop)

# Performs actions based on choice 

#define user list
user =[]

while True:
    print("Select the option which you want to perform:")
    print("1.Create a User")
    print("2.view all users")
    print("3.search user by name")
    print("4.Exit")

#Select option from user
    choice = int(input("Enter your choice:"))

#Add User Details
    if choice == 1:
        name = input("Enter Your Name:")
        age = int(input("Enter Your Age:"))
        salary = float(input("Enter your salary:"))
        is_employeed_input = input("Are you an employeed (yes/no)")
        is_employee = is_employeed_input

    user = {
        "name": name,
        "age": age,
        "salary": salary,
        "is_employee": is_employee
    }

    user.append(user)
    print("user created successfully.")