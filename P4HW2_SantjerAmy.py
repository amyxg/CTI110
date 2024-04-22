#Amy Santjer
#04/06/2024
#P4HW2
#The program however will calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

#Asks the user to enter name of employee or terminate to finish program
name = str(input("Enter employee's name or type 'Done' to terminate program: "))
numberOfEmployees = 0
totalOTPay = 0
totalRegPay = 0
totalGrossPay = 0

#Loop for employee(s) name, hours, and pay 
while name != "Done":
    hours = float(input(f"How many hours did {name} work? ")) #Ask user to enter number of hours the employee worked this week
    pay = float(input(f"What is {name}'s pay rate: ")) #Ask user to enter employee's pay rate
    #Evaluate if employee has worked overtime (more than 40 hours).
    if hours >= 40:
        overtime_hours = hours - 40
        gross_pay = ((hours - 40)*pay*1.5)+pay*40 
        regHour_pay = 40 * pay 
        overtime_pay =gross_pay - regHour_pay 
    elif hours <= 40:
        overtime_hours = 0
        overtime_pay = 0
        regHour_pay = (hours * pay)
        gross_pay = regHour_pay
    print("-----------------------------")
    print(f'{"Employee name:":<10} {name}\n')
    print(f'{"Hours worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay":<10}')
    print("-----------------------------------------------------------------------------------------")
    print(f'{hours:<15.1f}{pay:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<19.2f}${regHour_pay:<20.2f}${gross_pay:<10.2f}\n')
    numberOfEmployees += 1
    totalOTPay += overtime_pay
    totalRegPay += regHour_pay
    totalGrossPay += gross_pay
    name = str(input("Enter employee's name or type 'Done' to terminate program: "))
    #if function for when user input done instead of Done 
    if name == "done":
        fixInput = str(input("Uh Oh! Do you mean 'Done'? Y or N? " ))
        if fixInput == "Y":
            name = str(input("Please type 'Done' exactly as spelled: "))
        elif fixInput == "N":
            print("\nPlease re-type employee's name in the section below again!")
            name = str(input("Enter employee's name or type 'Done' to terminate program: "))

#Total results
print("")
print(f"Total number of employees entered: {numberOfEmployees}")
print(f"Total amount paid for overtime: ${totalOTPay:.2f}")
print(f"Total amount paid for regular hours: ${totalRegPay:.2f}")
print(f"Total amount paid in gross: ${totalGrossPay:.2f}")




