#Print header and separator
print("<-- Pangram Checker -->")
print("-----------------------")

#List to store (sentence, unique_letter_count) pairs
sentence_results = []
#Outer loop keeps collecting sentences until the user types "done"
while True:
    #Inner loop keeps re-prompting until a non-empty sentence is entered
    while True:
        sentence = input("Please enter a sentence (or 'done' to finish): ").strip().lower()
        #Check for the sentinel value first, before checking emptiness
        if sentence == "done":
            break
        if sentence == "":
            print("The sentence cannot be empty. Please try again.")
            continue
        break
    #Check the sentinel BEFORE doing any processing on this input
    if sentence == "done":
        break

    #Normalize the sentence
    normalized_sentence = [ch for ch in sentence if ch.isalpha()]
    #Join all the characters in the normalized sentence
    unified_sentence = ''.join(normalized_sentence)

    #Create list to store missing letters
    missing_letters = []
    #Loop over the unified sentence
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        #Set condition for the character not present in the unified sentence
        if ch not in unified_sentence:
            #Add the character to the missing letters list if it is not found in the unified sentence at least once
            missing_letters.append(ch)

    #Set condition for no missing letters
    if len(missing_letters) == 0:
        #Print the message that the sentence is a pangram
        print("The sentence you entered is a pangram.")
    #Set condition for existing missing letters
    else:
        #Print the message that the sentence is not a pangram and list the letters
        print("The sentence you entered is not a pangram. The following letters have not been used:")
        for i, ch in enumerate(missing_letters, start = 1):
            print(f" {i}. {ch}")

    #Create a list of (letter, count) pairs for every letter of the alphabet
    letter_counts = [(ch, unified_sentence.count(ch)) for ch in 'abcdefghijklmnopqrstuvwxyz']
    #Filter only the letters that appear more than 3 times
    frequent_letters = [(ch, count) for ch, count in letter_counts if count > 3]
    #Print the result
    if len(frequent_letters) == 0:
        print("No letter appears more than 3 times.")
    else:
        print("Letters appearing more than 3 times:")
        for i, (ch, count) in enumerate(frequent_letters, start=1):
            print(f" {i}. '{ch}' appears {count} times")

    #Get the unique letters
    uniques_letters = set(unified_sentence)
    #Add the sentence and the number of unique letters to the sentence results list
    sentence_results.append((sentence, len(uniques_letters)))

    print()

if len(sentence_results) == 0:
    print("No sentence entered.")
else:
    #Find the smallest unique-letter count across all sentences
    min_unique_count = min(sentence_results, key=lambda x: x[1])[1]
    #Collect every sentence that matches that minimum count
    fewest_unique_sentences = [s for s, count in sentence_results if count == min_unique_count]
    #Print result with singular/plural handling
    if len(fewest_unique_sentences) == 1:
        print(f"The sentence with the fewest unique letters ({min_unique_count}) is:")
        print(f" \"{fewest_unique_sentences[0]}\"")
    else:
        print(f"{len(fewest_unique_sentences)} sentences tied for the fewest unique letters ({min_unique_count}):")
        for i, s in enumerate(fewest_unique_sentences, start = 1):
            print(f" {i}. \"{s}\"")