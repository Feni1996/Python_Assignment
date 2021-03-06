"""Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers."""

def showNumber(limit):
    for i in range(0, limit+1):
        if i==0:
            print(i, "EVEN")
        elif i%2==0:
            print(i, "EVEN")
        else:
            print(i, "ODD")

showNumber(3)

"""Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)"""

a=list(range(1,21))
print(list(filter(lambda x:x%2==0, a)))

"""Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions."""

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x**2, list(filter(lambda x:x%2==0, a)))))

"""Write a function to compute 5/0 and use try/except to catch the exceptions"""

def fun1():
    try:
        i=5/0
    except ZeroDivisionError as e:
        print("Please Do not Devide by ZERO.!")
    except:
        print("Any other error.!")
fun1()

#13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce
import operator
l=['1','2','3','4','5','6','7']
s=reduce(operator.iconcat,l)
print(s)

"""14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions."""

print(list(filter(lambda x: x%3!=0 and x%7==0,range(1,21))))



"""15. Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation."""

def multi(n):
    return n*n

num=[1,2,3]
result=map(multi, num)
print(list(result))
#### OUTPUT----------------------------------------
"""def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)"""

#O/P: 2

#O/P: Error becouse f is not defined.


from itertools import zip_longest 

Num=[1,2,3] 
L = ['a','b'] 
Z=zip_longest(Num,L,fillvalue='#') 
print(list(Z)) 
