"""4. Create a Time class and initialize it with hours and minutes.
Create a method addTime which should take two Time objects and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Create another method displayTime which should print the time.
Also create a method displayMinute which should display the total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minute."""

class  Time():
    def __init__(self, hrs, mins):
        self.hrs = hrs
        self.mins = mins

    def addTime(t1, t2):
        t3 = Time(0, 0) # creating new object
        t3.hrs = t1.hrs + t2.hrs # sum of hours
        t3.mins = t1.mins + t2.mins # sum of minutes
        while t3.mins >= 60:
            t3.hrs += 1
            t3.mins -= 60
        return t3

    def displayTime(self):
        print(f"Time is {self.hrs} hours and {self.mins} minutes.")

    def displayMinutes(self):
        print((self.hrs * 60) + self.mins, "minutes.")

t1 = Time(2, 50)
t2 = Time(1, 20)
t3 = Time.addTime(t1, t2)
t3.displayTime()
t3.displayMinutes()