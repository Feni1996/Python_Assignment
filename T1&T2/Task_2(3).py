"""Write a program in Python to implement the given flowchart:"""

a=10; b=20; c=30
avg=(a+b+c)/3
print(f"Avg is {avg}")

if (avg>a and avg>b and avg>c):
    print("Avg is higher than a, b, and c.")

elif (avg>a and avg>b):
    print("avg is higher than a and b")

elif(avg>a and avg>c):
    print("Avg is higher than a and c.")

elif(avg>b and avg>c):
    print("Avg is higher than b and c.")

elif(avg>a):
    print("Avg is just higher than a.")
    
elif(avg>b):
    print("Avg is just higher than b.")

else:
    print("Avg is just higher than c.")

