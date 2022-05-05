# Program to find sum of array elements

size=int(input("Enter the number of elements you want in array: "))
arr=[]
sum=0

for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
    sum+=elem
print("Sum of array elements = ",sum)
