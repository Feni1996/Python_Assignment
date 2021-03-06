"""Write a program in Python to perform the following operation: 
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
string."""

a = int(input("Enter a Number: "))
if (a%3==0 and a%5==0):
    print("Consultadd- Python Training")
elif(a%5==0):
    print("Python Training")
elif(a%3==0):
    print("Consultadd")
else:
    print("Number is not divisible by 3 or 5.")


"""Write a program in Python to perform the following operator based task:"""


num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
print("Enter 1- Addition, Enter 2- Subtraction, Enter 3 - Division, Enter 4 - Multiplication, Enter 5 - Average")
option = int(input())

if (option==1): print("Add of two num: ",(num1+num2))
elif (option==2): print("Sub of two num: ",(num1 - num2))
elif (option==3): print("Div of two num: ",(num1/num2))
elif (option==4): print("Multi of two num: ",(num1*num2))
elif (option==5): print("Avg of two num: ",((num1+num2)/2))
else: print("Enter valid option.")