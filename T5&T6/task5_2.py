"""2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode."""

import sys

try:
    print("Enter a file name that you want to read: ", sys.argv[1])
    print("Number of argument: ", len(sys.argv))
    print("Name of file: ", str(sys.argv[1]))
    if str(sys.argv[1]) != 'a.txt':
        raise FileExistsError
except FileExistsError:
    print("Please enter a correct file name.")

else:
    with open(str(sys.argv[1])) as f:
        for line in f:
            print(line)
