# Program to insert element at a given location in Array

arr = [1, 2, 3, 4, 5]
num=int(input("Enter a number to insert in array : "))
index=int(input("Enter a index to insert value : "))
if index >= len(arr):
    print("please enter index smaller than",len(arr))
else:
    # insering element ‘num’ at ‘index’ position
    arr.insert(index, num) 
print('Áarry after inserting',num,"=",arr)