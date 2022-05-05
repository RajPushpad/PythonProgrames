# Program to delete element at end of array

print("Enter 10 Elements: ")
arr = []
for i in range(10):
    arr.append(input())

print("\nEnter the Value to Delete: ")
val = input()

arr.remove(val)

print("\nThe New list is:")
print(arr)