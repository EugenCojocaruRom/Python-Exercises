#Prompt user to enter message
message = input("Enter your message: ")

#Create empty list for shifted characters
shifted_chars = []
#Loop through the message string
for ch in message:
    #Set condition for uppercase character
    if ch.isupper():
        #Shift the character 3 letters to the right
        shift_ch = chr((ord(ch) - 65 + 3) % 26 + 65)
        #Add the shifted character to the list
        shifted_chars.append(shift_ch)
    #Set condition for lowercase character
    elif ch.islower():
        #Shift the character 3 letters to the right
        shift_ch = chr((ord(ch) - 97 + 3) % 26 + 97)
        #Add the shifted character to the list
        shifted_chars.append(shift_ch)
    #Set condition for any other character
    else:
        #Add the character as it is to the list
        shifted_chars.append(ch)
#Print the shifted characters
print(f"New message (_for loop_): {''.join(shifted_chars)}")

#Filter the shifted characters
shifted_chars = [chr((ord(ch) - 65 + 3) % 26 + 65) if ch.isupper() else chr((ord(ch) - 97 + 3) % 26 + 97) if ch.islower() else ch for ch in message]
#Print the shifted characters
print(f"New message (_list comprehension_): {''.join(shifted_chars)}")
