# Program of Palindrome or not using Iterative method 

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print(f"The Number is a palindrome!")
else:
    print("The number isn't a palindrome!")
 