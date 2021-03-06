"""Write a program in Python to find out the character in a string which is uppercase using list
comprehension."""

st = input("Enter a String with some Upper letter: ")

res = [char for char in st if char.isupper()]

print(f"The all upper case charecter are : {res}")

"""Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension."""

student=['Feni', 'Luv', 'Xyz']
subject=['Math', 'Sci', 'Phy']

## Using for loops....
#d={}
"""for keys in student:
    for value in subject:
        d[keys]=value
        subject.remove(value)
        break
print(d)"""

#Using Dic comp.............

res = {student[i]: subject[i] for i in range(len(student))}
print(res) 

# Learn More about Yield, next and Generators

# Generator : Used to create a custom iterator.
# Yield: used to pause ans save the item for next successive call using next().

# Write a program in Python using generators to reverse the string.

def rev_str(s):
    l=len(s)
    for i in range(l-1, -1, -1): # Starting from reverse position to 0 th index and each time -1 the index.
        yield s[i]
s1 = 'Consultadd Training'
for char in rev_str(s1):
    print(char,end='')

print("\n")
# Write an example on decorators.

# Decorater : take one function add some featues to it then return the original function
# Clauser: Function has one more function inside.

def star(fun):
    def inner(arg):
        print('*'*25)
        fun(arg)
        print('*'*25)
    return inner

def perc(fun):
    def inner(arg):
        print('%'*25)
        fun(arg)
        print('%'*25)
    return inner

@star
@perc
def display(msg):
    print(msg)

display("Welcome to Decorative..!")