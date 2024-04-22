#Amy Santjer
#03/11/2024
#P3HW2
#Calculating salary

#Asks the user to enter name of employee
name = str(input("Enter employee's name: "))

#Ask user to enter number of hours the employee worked this week
hours = float(input("Enter number of hours worked: "))

#Ask user to enter employee's pay rate
pay = float(input("Enter employee's pay rate: "))

#Evaluate if employee has worked overtime (more than 40 hours).
if hours >= 40:
    overtime_hours = hours - 40
    gross_pay = ((hours - 40)*pay*1.5)+pay*40 #calculate gross pay (total amount that should be paid to employee)
    regHour_pay = 40 * pay #Calculate amount employee should be paid for regular hours worked.
    overtime_pay =  (((hours - 40)*pay*1.5)+pay*40)-regHour_pay #Calculate the amount owed to employee for overtime hours
elif hours <= 40:
    overtime_hours = 0
    overtime_pay = 0
    gross_pay = ((hours - 40)*pay*1.5)+pay*40
    regHour_pay = (hours * pay)

print("-----------------------------")
print(f'{"Employee name:":<10} {name}\n')
print(f'{"Hours worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay":<10}')
print("-----------------------------------------------------------------------------------------")
print(f'{hours:<15.1f}{pay:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<19.2f}${regHour_pay:<20.2f}${gross_pay:<10.2f}')


