#Print header and separator
print("<-- SMS Message Splitter -->")
print("----------------------------")

#Prompt user to enter a message
message = input("Enter the message: ")
#Prompt user to enter the max character limit per part
message_part = int(input("How many characters per message part? "))

#Reserve space for a prefix like "(99/99) " — 8 characters
prefix_reserve = 8
#Calculate the usable length ofr a message part
usable_length = message_part - prefix_reserve

#Check that there is enough space to fit text after the numbering ("(x/y) ") prefix for each part
if usable_length <= 0:
    print("There is not enough space to fit any text after the prefix.")
else:
    #Split the message into parts based on the number of characters
    split_message = message.split()
    #Create empty list to hold the message parts
    message_parts = []
    #Declare variable for the current part and initialize it
    current_part = ""
    #Loop through the split message list
    for word in split_message:
        #Set condition for the case when the word is longer than the usable length
        if len(word) > usable_length:
            #Save the part that was built before the long word
            if current_part != "":
                message_parts.append(current_part)
                current_part = ""
            #Slice the long word into fixed-size chunks
            for start in range(0, len(word), usable_length):
                chunk = word[start:start + usable_length]
                message_parts.append(chunk)
        #Set condition for normal length words
        else:
            #Check how the possible message part would look like if adding the word
            if current_part == "":
                possible_part = word
            else:
                possible_part = current_part + " " + word
                #Check if the possible part still fits within the limit
            if len(possible_part) <= usable_length:
                current_part = possible_part  #It fits, so keep it
            else:
                message_parts.append(current_part)  #Save the finished part
                current_part = word  #Start a new part with this word
    #After the loop ends, add the last part if it's not null
    if current_part != "":
        message_parts.append(current_part)

    #Declare variable for the length of the message parts list
    num_parts = len(message_parts)
    #Loop over the message parts
    for i, part in enumerate(message_parts, start = 1):
        #Print each message part
        print(f"({i}/{num_parts}) {part}")

#Test 1: Hi there Supercalifragilisticexpialidocious friend --> 15
#Test 2: Hello Tim! Are we still on for that meeting you wanted to have at 6PM today? Thanks! --> 25