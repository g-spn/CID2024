# File: Password Strength Checker
# -----------------------------

"""
Based on USA Cybersecurity and Infrastructure Security Agency
Source: https://www.cisa.gov/secure-our-world/use-strong-passwords
"""

"""
Step 1:
    Define Password strenght Criterias
Step 2:
    Set up a way for user to input password
Step 3:
    Evaluate the password
    Create multiply function for each seperate criteria
Step 4: 
    Combine resule from evaluating difference criterias
Step 5:
    Display feedback
Step 6(optional):
    Calculate the entropy of the password which provides the lenght of time it would take to brute froce
    check users password to see if it's on the top used passwords


"""
def password_recommendations():
    #Currently a place holder, at a later date password recommedations or criterias will be posted.
    print("this is a place holder for password criterias")

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
    pass

def pwd_uppercase_char(pw_2_check):
    # Checks to see if string contains uppercase characters
    pass

def pwd_numerical_char(pw_2_check):
    # Checks to see if string contains numerical characters
    pass

def main():
    #   List password criterias for a strong password
    #   pw_variable used in main
    #   pwd_variable is used for functions
    
    #   Print's guidelines for strong passwords
    #password_recommendations()

    # Ask users for password to check
    pw_2_check = pwd_input()

    # use to help debug
    print("Back in main (printing input):" + str(pw_2_check))
    
    # check lenght of password
    pw_lenght = pwd_lenght(pw_2_check)
    
    # use to help depug
    print("main pw: " + str(pw_lenght))
    
    # check password string contains a special character
    pw_special_char = pwd_special_char(pw_2_check)
    
    # debug : check for results of special character
    #print(pw_special_char)

    

if __name__ == "__main__":
    main()
