db = open("output.txt", "a")

days = int(input("For how many days do you wan to measure the weather severity? "))
averageRain = [1]
averageWindSpeed = [1]
numberRain = float(input("What is the expected rain? (enter: -1.0 to end) "))
averageRain.append(numberRain)
numberWind = float(input("What is the expected wind? (enter: -1.0 to end) "))
averageWindSpeed.append(numberWind)
while numberRain > -1.0 and numberWind > -1.0:
    numberRain = float(input("What is the expected rain? (enter: -1.0 to end) "))
    averageRain.append(numberRain)
    numberWind = float(input("What is the expected wind? (enter: -1.0 to end) "))
    averageWindSpeed.append(numberWind)
    if numberRain == -1.0:
        break
    if numberWind == -1.0:
        break
windResults = sum(averageWindSpeed)/days
rainResults = sum(averageRain)/days
print("The average rain is", rainResults, "inches")
print("The average wind speed is", windResults)
print("The weather severity for these", days, "readings is", ((sum(averageRain)*10)+ sum(averageWindSpeed))/days)






