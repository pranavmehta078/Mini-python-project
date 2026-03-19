#This is the interest calculator,which will calculate the interest based on the principal amount, rate of interest and time period. 
#Define the variables for interest calculator

Principalamount = float(input("Please enter the principal amount :")) 
Rateofinterest  =  float(input("please enter the rate of interest:"))
Timeperiod = float(input("Please enter the time period in years :"))

#Calculate the interest
Interest = (Principalamount * Rateofinterest * Timeperiod) / 100

#Print the interest
print("The interest is:", Interest)