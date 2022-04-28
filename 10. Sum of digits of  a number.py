# Program of Sum of digits of a number

num = int(input("Enter a number"))
sum = 0
while num > 0:
    R = num%10
    sum = sum + R
    num = num //10
    print('\n sum of a digits = %d' %sum)
