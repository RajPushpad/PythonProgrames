# Program to Convert Decimal number into Binary


num = int(input("Enter Decimal Number:"))

tamp = 0
mul = 1
while num>0:
    rem = num%2
    tamp = tamp+(rem*mul)
    mul = mul*10
    num = int(num/2)

print("\nEquivalent Binary Value =", tamp)