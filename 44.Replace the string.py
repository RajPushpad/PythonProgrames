#Program the code to replace the string space with given character


string = input("Enter a String : ")
result = ''  
ch = input("Enter a Character : ")
for i in string:  #iterating using for loop
        if i == ' ':  
            i = ch   
        result += i   
print('String after removing space with t = ',result)
