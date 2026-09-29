#Define function for encoding
def encode(text):
    #Set condition for handling empty strings
    if text == "":
        return ""
    #Declare variable that holds an empty string
    encoded = ""
    #Declare a variable as counter and initialize it to 1
    count = 1
    #Loop through the indexes and individual characters of the text
    for i, char in enumerate(text):
        #Set condition for index 0
        if i == 0:
            #Skip index 0, as there is nothing to compare to
            continue
        #Set condition for the current character when it is the same as the one from the previous index
        elif char == text[i - 1]:
            #Increment the counter
            count += 1
        #Set condition for the other cases
        else:
            #Add the previous character to the encoded text + its count
            encoded += text[i - 1] + str(count)
            #Reset the counter to 1
            count = 1
    #Add the last group to the encoded text + its count
    encoded += text[-1] + str(count)
    return encoded

#Define function for decoding
def decode(compressed):
    #Declare variable that holds an empty string
    decoded = ""
    #Declare variable that holds the current letter
    current_letter = ""
    #Declare variable i for index and initialize it to 0
    i = 0
    #Loop through the length of the text for as long as the index < than the length of the text
    while i < len(compressed):
        #Declare variable with the value of the index
        char = compressed[i]
        #Set condition for the case when the character is a letter
        if char.isalpha():
            #Set the current letter to the value of the character
            current_letter = char
            #Increment the index by 1
            i += 1
        #Set condition for the case when the character is a digit
        else:
            #Declare variable that holds an empty string
            num = ""
            #Loop through the length of the text for as long as the index < than the length of the text and the character is a digit
            while i < len(compressed) and compressed[i].isdigit():
                #Add the character to the num string
                num += compressed[i]
                #Increment the index by 1
                i += 1
            #Add the previous character to the decoded text for as many times as the count indicates (convert num to integer)
            decoded += current_letter * int(num)
    #Return the decoded text
    return decoded

#Define function for handling encoded words that are shorter than the original
def compression_report(words):
    return [word for word in words if len(encode(word)) < len(word)]
print(f"Short words: {compression_report(['aaaa', 'abc', 'zzzzzz', 'hello'])}")

#Test the 2 functions with a list of strings
test_strings = ["aaabbc", "abc0", "wwwwwwwwww", "1", "", "hello", "a1b"]
for s in test_strings:
    if decode(encode(s)) == s:
        print(f'"{s}" - OK')
    else:
        print(f'"{s}" - FAIL')