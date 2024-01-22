# Python script to check the password strength
def check_password_strength(pwd):
    check=0  
    valid=1
    specialcharacters="~!@#$%^&*()_+=-,."

    if (len(pwd) < 8):
        print("Minimum length: The password should be at least 8 characters long.")
        valid=0
    
    if (str(pwd).isdigit() or str(pwd).isalpha()):
        print("Should contain alphabets (A-Z) and at least one digit (0-9)")
        valid=0
    
    if (str(pwd).islower() or str(pwd).isupper()):
        print("Should contain both uppercase and lowercase letters.")
        valid=0

    for i in str(pwd):
        if i in specialcharacters:
            check+=1         
    if check==0:        
        print("Should contain at least one special character.")
        valid=0
    
    if valid == 0:
        return False
    else:
        return True

def main():
    while (True):
        getPassword = input("Please enter the password: ")

        if check_password_strength(getPassword) == False:
            print("Password does not meet the above criteria.")
        else:
            print("Password is valid!")
            break

main()