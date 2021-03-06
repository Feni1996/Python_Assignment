"""Read doc.txt file using Python File handling concept and return only the even length string from
the file. Consider the content of doc.txt as given below:"""

with open('doc.txt') as f:
    for line in f:
        l=[]
        l=line.split(" ")
        for s in l:
            a=len(s)
            if a%2==0:
                print(s, end=" ")
            else:
                continue