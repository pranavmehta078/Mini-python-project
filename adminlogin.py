#This is showing the loginscript

Username = "pranav"
Password = "admin123"

#Enter the username and password from user
Uname = input("Enter the Username :")
Upassword =input("Enter the Password :")

#Compare with user entered uname and password with orignal one
if Username==Uname and Password == Upassword :
    print("User login successfully")
else:
    print("Incorrect username and password")