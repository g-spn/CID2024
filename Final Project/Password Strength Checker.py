# File: Password Strength Checker
# -----------------------------
import math

"""
Based on USA Cybersecurity and Infrastructure Security Agency
Source: https://www.cisa.gov/secure-our-world/use-strong-passwords

Step 1:
    Define Password strenght Criterias
Step 2:
    Set up a way for user to input password
Step 3:
    Evaluate the password
    Create multiply function for each seperate criteria
Step 4: 
    Combine results from evaluating difference criterias
Step 5:
    Display feedback
Step 6(optional):
    Calculate the entropy of the password which provides the lenght of time it would take to brute froce
    check users password to see if it's on the top used passwords
"""
def password_recommendations():
    # recommendation for strong passwords
    print("How to make a strong password")
    print(" Type 1: Random string \n	A string mixed-case letters, numbers, symbols")
    print("	A minimum 16 characters, longer is better")
    print(" examples:\n	Great: cXmnZK65rf*&DaaD \n	Amazing: Yuc8$RikA34%ZoPPao98t \n")
    print(" Type 2: Passphrases\n examples")
    print("	Good: HorsePurpleHatRun \n	Great: HorsePurpleHatRunBay \n	Amazing: Horse Purple Hat Run Bay Lifting\n")
    print("Entropy:\n	Weak: 	0-49\n	Good: 	50-70\n	Strong: 70-120\n	Very Strong: 120+ \n")

def pwd_input():
    #Request users to input a password
    pw_2_check = input("Please enter the password you would like to check: ")
    
    #ignore - used to help debug program. 
    #print("This is the users password in pwd_input function:" + str(pw_2_check))

    #return's password to be used for later
    return pw_2_check

def pwd_lenght(pw_2_check):
    #Obtain the len of the password as a value
    pw_lenght = len(pw_2_check)

    #print("function pwd_lenght" + str(pw_lenght))

    return pw_lenght

def pwd_special_char(pw_2_check):
    
    # Checks to see if string contains special character
    # Special character list obtain from 
    # https://owasp.org/www-community/password-special-characters

    special_char_list = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for i in pw_2_check:
        if i in special_char_list:
            #print(f"{i} is in list")
            return(True)
        #else:
            #print(f"{i} is not in the list")
    return(False)    

def pwd_lowercase_char(pw_2_check):
    # Checks to see if string contains lowercase characters
    for i in pw_2_check:
        if i.islower():
            #print(f"{i} is lower case")
            return(True)
        #else:
            #print(i)
    return(False)        

def pwd_uppercase_char(pw_2_check):
    # Checks to see if string contains uppercase characters
    for i in pw_2_check:
        if i.isupper():
            #print(f"{i} is upper case")
            return(True)
        #else:
            #print(i)
    return(False)        

def pwd_numerical_char(pw_2_check):
    # Checks to see if string contains numerical characters
    for i in pw_2_check:
        if i.isnumeric():
            #print(f"{i} is a number")
            return(True)
        #else:
            #print(i)
    return(False)

def pw_strenght_display(pw_2_check, pw_lenght ,pw_lowercase_char, pw_numerical_char, pw_uppercase_char, pw_special_char):
    #Bolean value for number only passwords
    pw_nums_only = pw_2_check.isnumeric()
    #displays weak, good, strong, very strong
    pw_count_true = sum([pw_lowercase_char, pw_numerical_char, pw_uppercase_char, pw_special_char])
    #print(pw_count_true) #debug: check value of all true/false values.
    
    #Puts common password in a list
    common_pw_list = check_for_common_pw("Final Project\\10k-most-common-pw.txt")

    if pw_2_check in common_pw_list:
        print("The password you entered is a common password") 
    if (pw_lenght > 37 and pw_nums_only == True) or (pw_lenght > 25 and pw_nums_only == False ) or (pw_lenght > 22  and pw_count_true == 2 ) or (pw_lenght > 19  and pw_count_true >= 3 ):
        print("Password strenght: Very Strong")
    elif(pw_lenght > 18 and pw_nums_only == True) or (pw_lenght > 12 and pw_lenght <= 24 and pw_count_true == 1 and pw_nums_only == False) or (pw_lenght > 10  and pw_count_true == 2 ) or (pw_lenght > 10  and pw_count_true == 3 ) or (pw_lenght > 9  and pw_count_true == 4 ):
        print("Password Strenght: Strong")
    elif(pw_lenght > 14 and pw_nums_only == True) or (pw_lenght > 10 and pw_lenght <= 12 and pw_count_true == 1 and pw_nums_only == False) or (pw_lenght > 8  and pw_count_true == 2 ) or (pw_lenght > 8  and pw_count_true == 3 ) or (pw_lenght > 7  and pw_count_true == 4 ):
        print("Password Strenght: Good")
    else:
        print("Password Strenght: Weak")
    
    # Calculates the entropy of the passwords.
    pw_entropy = pwd_entropy(pw_lenght ,pw_lowercase_char, pw_numerical_char, pw_uppercase_char, pw_special_char)
    print(f"Your password entropy is {pw_entropy:.1f}") 

def pwd_entropy(pw_lenght ,pw_lowercase_char, pw_numerical_char, pw_uppercase_char, pw_special_char):
    #Purpose is to calculate entropy
    #initalizing the variable
    character_pool_size = 0
    #If the following is true it increase character pool size variable
    if (pw_lowercase_char == True):
        #print("added 26 to pw_lowercase_char variable")
        character_pool_size += 26
    if (pw_numerical_char == True):
        #print("added 10 to pw_lowercase_char variable")
        character_pool_size += 10
    if (pw_uppercase_char == True):
        #print("added 26 to pw_lowercase_char variable")
        character_pool_size += 26
    if (pw_special_char == True):
        #print("added 32 to pw_lowercase_char variable")
        character_pool_size += 32
    #print(character_pool_size) 
    #formula to calcuate entropy
    pw_entropy = pw_lenght * math.log2(character_pool_size)
    return pw_entropy

def check_for_common_pw(filepath):
    #creates a list for appending words to list
    common_pw_list = []
    #command to open file and be read
    #each line read is erase and added to list
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                common_pw_list.append(cleaned_line)

    return common_pw_list

def main():
    #   List password criterias for a strong password
    #   pw_variable used in main
    #   pwd_variable is used for functions
    
    #   Print's guidelines for strong passwords
    print("Password Strenght Checker Program")
    print("Created by G-spn\n\n")
    password_recommendations()

    pw_2_check = None
    while True:
    # Ask users for password to check
        
        if pw_2_check == '':
            break
        else:
            pw_2_check = pwd_input()
            #print(f"Inputted password: {pw_2_check}") # use to help debug
            
            # check lenght of password
            pw_lenght = pwd_lenght(pw_2_check)
            #print("main pw: " + str(pw_lenght)) # debug: displays pw lenght
            
            # check password string contains a special character
            pw_special_char = pwd_special_char(pw_2_check)
            #print(f"Contains Special is : {pw_special_char}") # debug: check for results of pw_special_char

            #check password string contains lower case
            pw_lowercase_char = pwd_lowercase_char(pw_2_check)
            #print(f"Contains lower is :{pw_lowercase_char}") # debug: check for results of pw_lowercase_char
            
            #check password string contains upper case
            pw_uppercase_char = pwd_uppercase_char(pw_2_check)
            #print(f"Contains upper is : {pw_uppercase_char} ") # debug: check for results of pw_uppercase_char

            #check password string contains numerical char
            pw_numerical_char= pwd_numerical_char(pw_2_check)
            #print(f"Contains a number : {pw_numerical_char}") # debug: check for results of pw_numerical_char

            # display password strenght and Entropy
            pw_strenght_display(pw_2_check, pw_lenght , pw_lowercase_char, pw_numerical_char, pw_uppercase_char, pw_special_char)
            
            pw_2_check = input("Would you like to check another password?(hit enter to stop) ")
                           




if __name__ == "__main__":
    main()
