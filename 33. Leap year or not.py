# Program to Check the given year is a leap year or not

def CheckLeap(year):
    if (year %  4 == 0) :
        print("This year is Leap year ")
    else:
        print("This year is not a Leap year ")
year = int(input("Enter a year: "))
CheckLeap(year)