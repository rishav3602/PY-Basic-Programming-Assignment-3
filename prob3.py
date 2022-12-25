# 3.	Write a Python Program to Check Leap Year?


class LeapYearCheck:
    def __init__(self):
        self.year = int(input("Enter the year you want to check: "))
        
        if self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0):
            print(f"{self.year} is a leap year")
        else:
            print(f"{self.year} is not a leap year")

year = LeapYearCheck()
