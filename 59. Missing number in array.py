# Program to find missing number  in arry 


arr = []
n = int(input("Enter size of array:"))
for i in range(n-1):
    i = int(input("Enter element of arry: "))
    arr.append(i)
sum = (n*(n+1))/2
sumArr = 0
for j in range(n-1):
    sumArr = sumArr+arr[j]
print(int(sum-sumArr))