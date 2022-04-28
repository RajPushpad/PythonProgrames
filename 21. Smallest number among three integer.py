# Program of Smallest number of among three integer

a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
c = int(input("Enter number c : "))

if(a < b) and (a < c):
    min = a
elif(b < a) and (b < c):
    min = b
else:
    min = c
print('Smallest number: ',min)