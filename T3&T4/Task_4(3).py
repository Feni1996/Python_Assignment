def fun1(l):
    s=list(set(l))
    return s

print("Sorted List: ", fun1([2, 3, 4, 5, 3, 4, 5]))

"""Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically."""

i=[x for x in input().split("-")]
i.sort()
print("-".join(i))