# Program to add  two  number using recursion

def add(a, b):
    if b==0:
        return a
    else:
        return 1+add(a, b-1)

print("Enter Two Numbers: ", end="")
nOne = int(input())
nTwo = int(input())

res = add(nOne, nTwo)

print("\n" +str(nOne)+ " + " +str(nTwo)+ " = " +str(res))