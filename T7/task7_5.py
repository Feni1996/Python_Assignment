"""Write a Person class with an instance variable “age” and a constructor that takes an integer as a
parameter. The constructor must assign the integer value to the age variable after confirming the
argument passed is not negative; if a negative argument is passed then the constructor should set
age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
methods:"""

class Person:
    def __init__(self, age):
        if age<0:
            self.age=0
            print("Age is not valid, setting age to 0.")
        else:
            self.age=age

    def amIOld(self):
        if self.age>0 and self.age<13:
            print("You are Young.!")

        elif self.age>=13 and self.age<=19:
            print("You are Teenager..!!")
        
        else:
            print("You are Old..!!")

    def yearPasses(self):
        # Increment the age of the person in here  
        self.age+=1
        return self.age

age = int(input("Enter a age: "))         
p = Person(age)  
p.amIOld()
yr =int(input("Enter a year: "))
for j in range(0, yr):
    ag=p.yearPasses()  
print("Your Age will: ",ag)       
p.amIOld()

        
