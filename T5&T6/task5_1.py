"""1. Write a program in Python to allow the error of syntax to be handled using exception handling.
HINT: Use SyntaxError"""
try: 
    x=input("enter a num: ")
    if x.isalpha():
        raise SyntaxError
except SyntaxError:
    print("Something went wrong.There is a SyntaxError..!!")
else:
    print("djl")
finally:
    print("finally block: must execute.!!")


