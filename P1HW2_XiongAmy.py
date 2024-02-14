#Amy Xiong
#02/14/2024
#P1HW2
#Travel Expense Calculator

print("This program calculates and displays travel expenses\n")

budget = float(input('Enter Budget: $'))
location = str(input('Enter your travel destination: '))
fuel = float(input('How much do you think on will spend on gas? $'))
accomondation = float(input('Approximately, how much will you need for accomodation/hotel? $'))
food = float(input('Last, how much do you need for food? $'))

print("")
print("-------Travel Expenses-------")
print('Location:', location)
print('Initial Budget: $', budget, '\n')
print('Fuel: $', fuel)
print('Accomodation: $', accomondation)
print('Food: $', food, '\n')

print('Remaining Balance: $', budget - (fuel + accomondation + food))
