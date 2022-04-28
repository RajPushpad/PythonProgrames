# Program of Greatest among three integer

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter threed number: "))

if(num1 > num2) and (num1 > num3):
    max = num1
elif(num2 > num3) and (num2 > num3):
    max = num2
else:
    max = num3
    print('Greatest number is ',max)
