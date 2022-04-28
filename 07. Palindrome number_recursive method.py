# Program of Palindrome using recursive method   

def pal(n,t):
      if n == 0:
              return t
      t = (t*10) +(n%10)
      return pal(int(n/10),t)
num = int(input("Enter any number: "))
tamp = 0 
p = pal(num,tamp)
if(num==p):
       print(num,"is a palindrom number")
else:
       print(num,"is not a palindrom numbwer")