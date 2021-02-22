# Code to check if a year is leap or not

year = int(input("Which year do you want to check?\n"))

if year % 4 == 0 and year % 100 != 0:
    print('leap year')
    
elif year % 400 == 0 :
    print('leap year')

else:
    print('not a leap year')

#you can  also use nested if statements to achieve same results.
  
