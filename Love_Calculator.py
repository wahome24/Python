#love Calculator
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.

#For Love Scores less than 10 or greater than 90, the message should be:

#"Your score is **x**, you go together like coke and mentos."

#For Love Scores between 40 and 50, the message should be:

#"Your score is **y**, you are alright together."

#Otherwise, the message will just be their score. e.g.:

#"Your score is **z**."

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combined_name = name1+name2


T= combined_name.count('t')
R= combined_name.count('r')
U= combined_name.count('u')
E= combined_name.count('e')

total1 = T+R+U+E

L= combined_name.count('l')
O= combined_name.count('o')
V= combined_name.count('v')
E= combined_name.count('e')

total2 =  L+O+V+E

total = str(total1) + str(total2)

result = int(total)


if result < 10 or result >90:
    print('Your score is {} you do not go well together!'.format(result))
    
elif result >= 40 and result <=50:
    print('Your score is {} you are a great match!'.format(result))

else:
    print('Your score is {}'.format(result))
