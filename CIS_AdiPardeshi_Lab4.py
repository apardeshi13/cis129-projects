# Module 4 Lab-4
# Adi Pardeshi
# 21st February 2024
# The program below is a function retail() that determines the
# bonus for company and bonus for individual employee bonus
# it does so by taking input for monthly sales and the increase%
# in the amount of sales

# Define function
def retail():
    # This code obtains the monthly sales in the form of a float
    monthlySales = float(input("Enter Monthly Sales: "))
    # This code determines the store bonus based on the value of monthly sales
    if monthlySales >= 110000:
        storeAmount = 6000
    elif 110000 >= monthlySales >= 100000:
        storeAmount = 5000
    elif 100000 >= monthlySales >= 90000:
        storeAmount = 4000
    elif 90000>= monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    # This code obtains the sales increase in the form of a float
    salesIncrease = float(input("Sales Increase: "))
    salesIncrease = salesIncrease/100
    # This code determines the individual employee bonus based on the sales increase
    if salesIncrease >= .05:
        empAmount = 75
    elif .05 >= salesIncrease >= .04:
        empAmount = 50
    elif .04 >= salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    # This code outputs the employee store bonus and employee bonus
    # along with a message if the highest amount of bonus was achieved
    # for both values
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    # Checking if the highest amount of bonus was achieved
    if(storeAmount == 6000) and (empAmount == 75):
        print("Congrats! You have reached the highest bonus amounts possible!")
    # Return function
    return
# Call function
retail()