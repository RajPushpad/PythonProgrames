# Program of prime number is not

def PrimeChecker(a):  
    if a > 1 :
        for i in range(2, int(a/2) + 1):  
            if (a % i) == 0:  
                print("This is not a prime number:",a)  
                break    
        else:  
            print( " This is a prime number:",a)  
    else:  
        print( "This is not a prime number")   
a = int(input("Enter an input number:"))    
PrimeChecker(a) 