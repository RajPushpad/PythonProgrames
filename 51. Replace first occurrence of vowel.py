# Program to Replace First Occurrence of vowel with '-'in string

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")
string2 = ''
length = len(string)
for i in range(length):
    if(string[i] == char):
        string2 = string[0:i] + string[i + 1:length]
        break
 
print("Original String :  ", string)
print("Final String :     ", string2)