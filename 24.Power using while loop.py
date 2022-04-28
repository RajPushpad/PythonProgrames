# Program the power using ‘while-loop’

base = int(input("Enter the value for base :"))
exponent = int(input("Enter the value for exponent :"))
result=1;
print(base,"to the power ",exponent,"=",end = ' ')
while exponent != 0:
    result = base * result
    exponent-=1
print(result)