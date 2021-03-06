"""Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times."""

count=0
while count<3:
    uname=input('Enter username: ')
    pswd=input('Enter password: ')

    if pswd=='admin' and uname=='admin':
        print('Access granted')
        break

    else:
        print('Access denied. Try again.')
        count+=1
if count==3: print("You tried all your attemp.!! SORRY.!! TRY AGAIN.!!")

#DONE: Go through the link provided below to understand finally and raise concept:
