# Program to check given character is vowel or consonant

Ch=input("Enter a character to check vowel or consonant :" ) 
if(Ch == 'a' or Ch == 'e' or Ch == 'i' or Ch == 'o' or Ch == 'u' or Ch == 'A' or Ch == 'E' or Ch == 'I' or Ch == 'O' or Ch == 'U'):
	#if ‘if’ condition satisfy
	print('Given character', Ch ,'is vowel')
else: 
#if ‘if’ condition does not satisfy the condition
	print('Given character',Ch, 'is  consonant')