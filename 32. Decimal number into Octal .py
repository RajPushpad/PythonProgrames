# Program to Convert Decimal number to Octal number

num = int(input('Enter a Decimal number to Convert into Octal:'))
n=num
octal=0
i=0

while n!=0:
    rem = n%8
    octal = octal + rem * (10**i)
    n = n // 8
    i+=1

print('Octal Number=',octal)
    