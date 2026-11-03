#Get the alphabet
import string

#Print header and separator
print("<== Secret Message Decoder Ring ==>")
print("-----------------------------------")

#Create function for performing the encoding
def encode(text, shift=0):
    result = []
    for ch in text.lower():
        if ch in letter_to_number:
            result.append((letter_to_number[ch] -1 + shift) % 26 + 1)
    return result

#Create function for performing the decoding
def decode(numbers, shift=0):
    return "".join(number_to_letter[(n - 1 + shift) % 26 + 1] for n in numbers)

#Loop over the alphabet
for number, letter in enumerate(string.ascii_lowercase, 1):
    print(number, letter)

#Create empty dictionary for storing the number to letter pairs
letter_to_number = {}               #letter_to_number = {letter: number for number, letter in enumerate(string.ascii_lowercase, start=1)}
#Loop over the alphabet
for number, letter in enumerate(string.ascii_lowercase, 1):
    letter_to_number[letter] = number

#Create dictionary for storing the letter to number pairs (reverse)
number_to_letter = {number: letter for letter, number in letter_to_number.items()}

#Loop for validating the shift value
while True:
    try:
        #Prompt user to enter a shift in the letters
        shift = int(input("Enter a shift (0 for none): "))
        break
    except ValueError:
        print("Please enter a whole number.")

#Loop for validating the user input
while True:
    #Prompt user to enter a text or a sentence
    user_input = input("Enter a text / sentence: ")
    #Call the encode() function on the user input
    encoded_text = encode(user_input, shift)
    if encoded_text:
        break
    print("No letters found. Please try again.")

#Set condition for non-empty encoded text
if encoded_text:
    #Print the encoded user input
    print(f"Encoded text: {encoded_text}")
    #Print the sum of all the numbers resulting from the encoded text
    print(f"Sum after encoding: {sum(encoded_text)}")

    #Find and print the letter with the highest value (the letter furthest along in the alphabet) in the sentence/text
    highest_letter = max(encoded_text)
    print(f"Highest letter: {number_to_letter[highest_letter]} ({highest_letter})")

    #Decode the encoded text and print whether the result is the same as the original
    original_letters = "".join(ch for ch in user_input.lower() if ch in letter_to_number)
    print("Decoding OK:", decode(encoded_text, -shift) == original_letters)
#Set condition for empty encoded text
else:
    print("No letters found in the text. Please try again with some letters.")
