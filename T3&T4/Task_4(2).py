def fun1(s):
    u=0
    l=0
    for ch in s:
        if ch.isupper():
            u+=1
        elif ch.islower():
            l+=1
        else:
            pass

    print("No. of Uppercase: ",u," No. of Lowercase: ",l)

fun1("abcABCD")