#Print information about the password
print("About the password:\n"
      " -> Must be at least 8 characters long\n"
      " -> Must contain at least one number (0 - 9)\n"
      " -> Must contain at least one uppercase letter")

#Set condition
while True:
    #Prompt user to enter the password
    password = input("Please enter your password: ")
    #Check that the password length is correct
    if len(password) < 8:
        #Print message
        print("Too short! The password must be at least 8 characters long")
        continue

    #Check that the password contains at least one number
    if not any(char.isdigit() for char in password):
        #Print message
        print("The password must contain at least one number!")
        continue

    #Check that the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        #print message
        print("The password must contain at least one uppercase letter!")
        continue
    #Print message that the password is valid
    print("The password is correct!")
    break