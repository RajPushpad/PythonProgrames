# Program of Swap two numbers without using third variable

x = int(input("Enter a number:"))
y = int(input("Enter a number:"))

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)