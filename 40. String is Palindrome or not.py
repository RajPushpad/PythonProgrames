# Program to Check the String is Palindgrome or not


string = input("Please give a String : ")
if(string == string[:: - 1]):
   print("Given String is a Palindrome")
else:
   print("Given String is not a Palindrome")