#Create method for encoding the message (attributes: message, shift)
def encode(message, shift):
    #Create empty list for shifted characters
    shifted_chars = []
    #Loop through the message string
    for ch in message:
        #Set condition for letters
        if ch.isalpha():
            #Declare variable for the base value
            base = 65 if ch.isupper() else 97
            # Shift the character to the right by the value of 'shift'
            shift_ch = chr((ord(ch) - base + shift) % 26 + base)
            #Add the shifted character to the list
            shifted_chars.append(shift_ch)
        #Set condition for any other character
        else:
            #Add the character as it is to the list
            shifted_chars.append(ch)
    #Return the shifted characters
    return ''.join(shifted_chars)

#Create method for decoding the message (attributes: message, shift)
def decode(message, shift):
    #Return the decoded message
    return encode(message, -shift)

#Create method for returning the indexes where the two strings differ
def changed_positions(original, encoded):
    return [i for i, ch in enumerate(original) if ch != encoded[i]]

# ------- Test code -------
#Prompt user to enter message
message = input("Enter your message: ")
#Prompt user to enter the value for the letter shift
shift = int(input("Enter the number of characters for the shift: "))

#Encode and decode the message
encoded = encode(message, shift)
decoded = decode(encoded, shift)
#Print the encoded message
print("Encoded: ", encoded)
#Print the decoded message
print("Decoded: ", decoded)
#Print the indexes of the characters that changed positions
print("Indexes of changed positions: ", changed_positions(message, encoded))

#Brute force on an encoded string
secret_message = input("\nEnter the message to decode: ")
#Try every shift from 1 to 25 (shift 26 would repeat shift 0)
for n in range(1, 26):
    print(f"Shift {n}: {decode(secret_message, n)}")