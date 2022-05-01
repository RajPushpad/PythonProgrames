# program to print the highest frequency character in a string


string = input("Enter some text: ")

# Set frequency as empty dictionary
frequency_dict = {}

for character in string:
    if character in frequency_dict:
        frequency_dict[character] += 1
    else:
        frequency_dict[character] = 1

p = max(frequency_dict, key=frequency_dict.get)

print("\nMost occuring character is: ", p)
print("It is repeated %d times" %(frequency_dict[p]))