#Amy Santjer
#03/27/2024
#P4LAB2
#This is a program that whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.

#Get input from user
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

#while num1 is larger, allow user to re-enter
while num1 >= num2:
    print("ERROR: Second integer can't be less than the first. Please try again.\n")
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))

#If input is num1 < num2, conduct loop below
for number in range(num1, num2 + 1, 5): #range = start from num1 and end at numb2 + 1, in increments of 5
            print(number, end=" ") #Print in same line with spacing
        
