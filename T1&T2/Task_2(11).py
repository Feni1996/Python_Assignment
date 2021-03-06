ct = 1
while(ct<=5):
    num=int(input("Enter a Number: "))
    if num == 5:
        print("Good guess")
        break
    else:
        print("Try Again")
    
    ct+=1
if ct==6: print("Sorry but that was not very successful.!!")