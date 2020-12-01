#This short program displays the month of the year based on user input.

import calendar

print('To get the monthly calendar, just put the month number!')
print()
user = int(input('Enter month number(1-12): '))

while user != 'stop':
  if user >=1 and user <=12:
    result = calendar.month(2020,user)
    print(result)
  else:
    print('Out of range!Try again!')
  
  user = int(input('Enter month date(1-12): '))
  
  #it can be advanced by also asking the user to input their desired year.
