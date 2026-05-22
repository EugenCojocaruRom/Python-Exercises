#Prompt user to enter the text to encode
text1 = input("Enter text to encode: ")

#Define function for encoding
def encode(text1):
    #Declare variable that holds an empty string
    encoded = ""
    #Declare a variable as counter and initialize it to 1
    count = 1
    #Loop through the indexes and individual characters of the text
    for i, char in enumerate(text1):
        #Set condition for index 0
        if i == 0:
            #Skip index 0, as there is nothing to compare to
            pass
        #Set condition for the current character when it is the same as the one from the previous index
        elif char == text1[i - 1]:
            #Increment the counter
            count += 1
        #Set condition for the other cases
        else:
            #Set condition for count > 1
            if count > 1:
                #Add the previous character to the encoded text + its count
                encoded += text1[i - 1] + str(count)
            #Set condition for count < 1
            else:
                #Add only the previous character to the encoded text
                encoded += text1[i - 1]
            #Reset the counter to 1
            count = 1
    #Set condition for the last group of characters in the text, when the count > 1
    if count > 1:
        #Add the previous character to the encoded text + its count
        encoded += text1[-1] + str(count)
    #et condition for count < 1
    else:
        #Add only the previous character to the encoded text
        encoded += text1[-1]
    #Return the value of the encoded text
    return encoded
#Print the encoded text
print(f"The encoded text is: {encode(text1)}")

#Prompt user to enter the text to decode
text2 = input("Enter text to decode: ")
#Define function for encoding
def decode(text2):
    #Declare variable that holds an empty string
    decoded = ""
    #Declare variable i for index and initialize it to 0
    i = 0
    #Loop through the length of the text for as long as the index < than the length of the text
    while i < len(text2):
        #Declare variable with the value of the index
        char = text2[i]
        #Set condition for the case when the character is a letter
        if char.isalpha():
            #Add the character to the decoded text
            decoded += char
            #Increment the index by 1
            i += 1
        #Set condition for the case when the character is a digit
        elif char.isdigit():
            #Declare variable that holds an empty string
            num = ""
            #Loop through the length of the text for as long as the index < than the length of the text and the character is a digit
            while i < len(text2) and text2[i].isdigit():
                #Add the character to the num string
                num += text2[i]
                #Increment the index by 1
                i += 1
            #Convert the value of the num string to an integer
            count = int(num)
            #Add the previous character to the decoded text for as many times as the count indicates (-1 because we already added the letter once above)
            decoded += text2[i - len(num) - 1] * (count - 1)
    #Return the decoded text
    return decoded
#Print the decoded text
print(f"The decoded text is: {decode(text2)}")