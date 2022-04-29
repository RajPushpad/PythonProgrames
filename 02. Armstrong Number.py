# Program to Armstrong Number or not

num = int(input("Please Enter a Number: "))
temp = 0
n = num 
P = len(str(num))
while n > 0:
    digit = n % 10
    temp += digit ** P
    n = n//10
if num == temp:
    print('This Number is a Armstrong Number')
else:
    print('This Number is Not a Armstrong Number')