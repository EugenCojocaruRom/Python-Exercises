#Define function for checking if 2 words are anagrams of each other
def are_anagrams(word1, word2):
    #Convert the 2 words to lowercase
    word1 = word1.lower()
    word2 = word2.lower()
    #Sort the letters of each word into lists
    sorted_word1 = sorted([char for char in word1 if char.isalpha()])
    sorted_word2 = sorted([char for char in word2 if char.isalpha()])
    #Check if the 2 words have the same length
    if len(sorted_word1) != len(sorted_word2):
        #Print message
        print("The 2 words have different lengths.")
        return False
    #print section title
    print("Comparing the letters in the 2 words:")
    #Compare the words letter by letter
    for i, char in enumerate(sorted_word1):
        #Set condition for the case when the character in word 1 does not match the character in word 2
        if char != sorted_word2[i]:
            #Print message
            print(f"{i + 1}. {char} != {sorted_word2[i]} ✗")
            return False
        #Set condition for matching characters
        else:
            #Print message
            print(f"{i + 1}. {char} == {sorted_word2[i]} ✓")
    return True

#Prompt user to enter word 1
word1 = input("Enter the first word: ")
#Prompt user to enter word 2
word2 = input("Enter the second word: ")

#Declare variable to hold the result of the called function
result = are_anagrams(word1, word2)
#Set condition for the case when the 2 words are anagrams of each other
if result:
    #Print message
    print(f'✅ "{word1}" and "{word2}" ARE anagrams!')
#Set condition for the case when the 2 words are not anagrams of each other
else:
    #Print message
    print(f'❌ "{word1}" and "{word2}" are NOT anagrams.')
