"""Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included)."""

n=int(input("Enter a number: "))
d={}
for i in range(1, n+1):
    d[i]=(i*i)
print(d)