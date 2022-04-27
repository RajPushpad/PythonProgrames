# Program to reverse a number

num = int(input('Enter a number: '))
reversed = 0
n = num
while n!=0:
    reversed = reversed*10 + n%10;
    n = n//10
print("reversed number:",reversed)