#Amy Santjer
#02/23/2024
#P2HW2
#Grade Calculator / Lists

#Asks the user to enter grades for following tests
mod1 = float(input('Enter your grade for Module 1: '))
mod2 = float(input('Enter your grade for Module 2: '))
mod3 = float(input('Enter your grade for Module 3: '))
mod4 = float(input('Enter your grade for Module 4: '))
mod5 = float(input('Enter your grade for Module 5: '))
mod6 = float(input('Enter your grade for Module 6: '))

#Combine all grades into a single list
moduleList = [mod1, mod2, mod3, mod4, mod5, mod6]

#Find the length of the list
num_moduleList = len(moduleList)

#Find the element in the list with the smallest value
gradeLowest = min(moduleList)

#Find the element in the list with the largest value
gradeHighest = max(moduleList)

#Find the sum of all elements of a list (numbers only)
gradeSum = sum(moduleList)

#Find the average of a list (numbers only)
gradeAvg = gradeSum / num_moduleList

#Results
print("")
print("--------------Results----------------")
print(f'{"Lowest Grade:":<20}{gradeLowest:.1f}')
print(f'{"Highest Grade:":<20}{gradeHighest:.1f}')
print(f'{"Sum of Grades:":<20}{gradeSum:.1f}')
print(f'{"Average:":<20}{gradeAvg:.2f}')
print("-------------------------------------", '\n')
