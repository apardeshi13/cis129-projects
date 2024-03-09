def bottles():
    totalBottles = 0
    todayBottles = 0
    totalPayout = 0
    keepGoing = 'y'

    while keepGoing == 'y':
        counter = 1
        while counter <= 7:
            todayBottles = int(input("Enter the number of bottles collected on day "+ str(counter)+": "))
            totalBottles += todayBottles
            counter += 1

        totalPayout = totalBottles * 0.10

        print("Total bottles collected for the week: ", totalBottles)
        print("Total payout: $", round(totalPayout, 2))
        keepGoing = input("Do you want to enter another week’s worth of data?(y/n)")
        if keepGoing.lower() != 'y':
            break
bottles()