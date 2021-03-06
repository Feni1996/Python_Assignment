"""Write a program that accepts a string as an input from the user and calculate the number of digits
and letters."""

st=input("Enter a string: ")
l=0
d=0
for c in st:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)