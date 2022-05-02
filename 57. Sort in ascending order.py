# Program to sort string character in ascending order

string = input("Enter the string : ")
strList=list(string) 
sortedString=''.join(sorted(strList)) 
print("String Sorted in ascending order :", sortedString)
