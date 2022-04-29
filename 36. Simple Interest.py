# Program to Calculate Simple Interest with explanation


principal = int(input("Enter the principal amount: "))  
rate = int(input("Enter the rate of interest: "))  
time = int(input("Enter the time of interest in year: "))  
simpleInterest = (principal*rate*time)/100
print("Simple Interest = ",simpleInterest)