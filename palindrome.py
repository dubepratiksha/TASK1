#Write a function that tests whether a string is a palindrome.
string = "Kayak";  
flag = True;   
   
string = string.lower();  
   
for i in range(0, len(string)//2):  
    if(string[i] != string[len(string)-i-1]):  
        flag = False;  
        break;  
   
if(flag):  
    print("Given string is palindrome")  
else:  
    print("Given string is not a palindrome")