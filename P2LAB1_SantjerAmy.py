#Amy Santjer
#02/21/2024
#P2LAB1
#Driving Costs (Variables and Expressions)

#Get info from User
gasMileage = float(input("Enter the car's mpg: "))
costOfGas = float(input("Enter the cost for a gallon of gas: $"))

#Calculate the cost to drive 20, 75, 500 miles
mile20 = (20 / gasMileage) * costOfGas
mile75 = (75 / gasMileage) * costOfGas
mile500 = (500 / gasMileage) * costOfGas

print ("\n")
print (f"The cost to drive 25 miles is ${mile20:.2f}\n")
print (f"The cost to drive 75 miles is ${mile75:.2f}\n")
print (f"The cost to drive 500 miles is ${mile500:.2f}")
