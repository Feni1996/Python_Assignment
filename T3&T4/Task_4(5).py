"""Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized."""

lines = []
while True:
    l = input("Enter a sequence of lines: ")
    if l:
        lines.append(l.upper())
    else:
        break

for l in lines:
    print(l)


"""Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console."""

def addFun(a,b):
    print("Sum of two numbers: ",(int(a)+int(b)))

a=input("Enter a first no: ")
b=input("Enter a second no: ")
addFun(a, b)

"""Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line."""

def printVal(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 > l2:
        print("String is : ",s1, "Length is: ",l1)
    elif l1 < l2:
        print("String is : ",s2, "Length is: ",l2)
    else:
        print(s1)
        print(s2)

s1,s2=input().split()
printVal(s1,s2)