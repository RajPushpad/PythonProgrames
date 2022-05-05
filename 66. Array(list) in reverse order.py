# Program to print array(list) in reverse order

size = int(input("Enter the number of element you want in array: "))
arr = []
for i in range(0,size):
        element = int(input("Please given the value for index  "+str(i)+": "))
        arr.append(element)
print("Array in reverse order")
for i in range(size-1,-1,-1):
        print(arr[i])