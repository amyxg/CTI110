#Amy Santjer
#02/21/2024
#P2LAB2
#Simple Statistics

#ask user for numbers
num1 = float(input("Enter a float: "))
num2 = float(input("Enter a float: "))
num3 = float(input("Enter a float: "))
num4 = float(input("Enter a float: "))

#calculate a product and the mean of all the numbers
value = num1 * num2 * num3 * num4
value2 = (num1 + num2 + num3 + num4) / 4


#output
print("\n")
print(f'The product average is {value:.0f}')
print(f'The average of the numbers are {value2:.0f} \n')
print(f'The product average is {value:.3f}')
print(f'The average of the numbers are {value2:.3f}') 

