"""
January 10, 2023, Python Lab 1, ITEC 2905-80 Capstone

Write a program that asks for your name and the month you were born in
Your program should print 
A greeting to you, using your name
A message with the number of letters in your name
A 'Happy birthday month!' message if you were born in January
Bonus question – can you detect if the month entered is the same as the current month, no matter when you run the program?
"""
# User name input
name = input('Hello, please enter your name: ')

#Validation for empty name variable
while len(name) == 0:                                           
    print('Please enter at least one character ')
    name = input('Enter your name: ')

# User birth month input
birth_month_from_user = input('Please enter name of the month you were born in: ')
birth_month = birth_month_from_user.strip().lower()         # Striping the whitespace and making month all lowercase

# List of Classes
classes_taken = []
classes_taken_by_user = input('What is the class code and name of your first class for this semester?: ')

# TODO Finish adding to list, loop over each list item
classes_taken.append(classes_taken_by_user)             # 

print(f'Hello {name}!')             # String formatting

letters_in_name = len(name)         #Length of characters in 'name'

print(f'You have {letters_in_name} letters in your name.')              # String formatting for length of name

if birth_month == 'january':
    print('Happy Birthday to you this month!')
else:
    print(f'I hope you have a Happy Birthday in {birth_month.upper()} !')

# TODO Add Functions for flow control
print('End of program. Thank you')