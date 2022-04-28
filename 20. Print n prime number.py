# Program to print n prime number
  
Number = int(input(" Please Enter any Number: "))
 
print("Prime numbers between", 1, "and", Number, "are:")
 
for num in range(1, Number + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)