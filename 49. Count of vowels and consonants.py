# program to count occurrences of vowels and consonants in a string 



string = input("Enter a String : ")   
vowels = 0  
consonants = 0
for i in string:   
    if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):  
        vowels+=1 
    elif i.isalpha():  
        consonants+=1  
print("Vowels :",vowels,"Consonants:",consonants)
