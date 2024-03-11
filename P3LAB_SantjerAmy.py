#AmySantjer
#03/11/2024
#Write a program that takes in a year and determines whether that year is a leap year.


is_leap_year = False
   
input_year = int(input("Enter a year: "))


#if input is divisible by 400 or 4 & 100 leaving a 0 remainder.
# %100 if the year is a century year or not 
if ((input_year%400 == 0) or ((input_year%4 == 0) and (input_year%100 != 0))):
    is_leap_year != False 
    print(f'{input_year} - leap year')
else: 
    print(f'{input_year} - not a leap year')
    
