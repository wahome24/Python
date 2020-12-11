#Beginner simple reg/login system

data={} #stores user details when they sign up

print('Welcome to the Gaxhi online!')
print()

#Get user input.
user = input('Select action: sign up or login? ').lower()

#while loop ensures the program continues running until it breaks.

while user != 'stop':
  if user == 'sign up': #Allows user sign up
    username = input('Enter username: ')
    password = input('Enter password: ')
#matches the user username to the password provided.
    data[username]=password

  else: #allows for user login
    username = input('Enter username: ')
    password = input('Enter password: ')
#validation to ensure the details provided matches with those in record.
    if username in data and data[username]==password:
      print(f'Welcome, you are logged in as {username}')
      break
    else:
      print('credentials do not match or dont exist,try again')
  user = input('Select action: sign up or login? ').lower()
