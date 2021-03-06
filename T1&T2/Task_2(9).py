#number = -1
again = "yes"
while (again != "no"):
    number = input("Guess the lucky number: ")
    if number == '5':
        again="no"
    else:
        print ("That is not the lucky number")
        again = input("Would you like to guess again? ")