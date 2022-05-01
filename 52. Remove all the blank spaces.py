# Program to remove all the blank spaces in a given string


string = input("Enter a String : ")
result=''
for i in string:
    if i!=' ':
        result += i
print("String after removing the spaces :",result)

