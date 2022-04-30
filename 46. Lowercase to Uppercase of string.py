# program to convert lowercase char to uppercase of string

string = input("Enter a String : ")
result=''
for i in string:  
        if i.islower():  
            i = i.upper() 
        result += i 
print("String after converting lower case to upper :",result)
