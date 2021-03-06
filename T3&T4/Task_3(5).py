"""Create a new list which contains the specified numbers after removing the even numbers from a
predefined list."""

l1=list(range(20))
l2=list(x for x in l1 if x%2!=0)
print(f"Predefine List: {l1}")
print("After removing even num: ",l2)
