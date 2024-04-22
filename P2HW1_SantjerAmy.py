#Amy Santjer
#02/14/2024
#P2HW1
#Travel Expense Calculator

budget = float(input('Enter Budget: '))
location = str(input('Enter your travel destination: '))
fuel = float(input('How much do you think on will spend on gas? '))
accomodation = float(input('Approximately, how much will you need for accomodation/hotel? '))
food = float(input('Last, how much do you need for food? '))

print("")
print("--------------Travel Expenses-------------")
print(f'{"Location:":<20} {location}')
print(f'{"Initial Budget:":<20} ${budget:.2f}')
print(f'{"Fuel:":<20} ${fuel:.2f}')
print(f'{"Accomodation:":<20} ${accomodation:.2f}')
print(f'{"Food:":<20} ${food:.2f}')
print("-------------------------------------------", '\n')

balance = budget - (fuel + accomodation + food)

print(f'{"Remaining Balance:":<20} ${balance:.2f}')
