"""Write a program to handle an error if the user entered a number more than four digits it should
return “The length is too short/long !!! Please provide only four digits”"""


num = 4
while True:
    try:
        di = input("Enter a four digit number: ")
        l=len(di)
        if l<num or l>num:
            raise ValueError
        else:
            break   
    except ValueError:
        print("You entered less or more then four digit.!")

print(f"You entered 4 digit number is : {di}")