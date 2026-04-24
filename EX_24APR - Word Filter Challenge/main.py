#Display message for user
num_words = int(input("Enter number of words: "))
#Create empty list to hold the words
word_list = []
#Loop through the number of words
for i in range(num_words):
    #Read each word from the console
    word = input(f"Enter word {i + 1}: ")
    #Add each word to the list
    word_list.append(word)
#Print the word list
print(f"The words are: {', '.join(word_list)}")

#Filter the words that have more than 4 letters
filtered_words = sorted([x for x in word_list if len(x) > 4])
#Print filtered list
print(f"The filtered list is: {', '.join(filtered_words)}")

#Print section title
print("Individual words and their length:")
#Loop through the filtered words
for word in filtered_words:
    #Print each word along with its length
    print(f" --> {word} ({len(word)} letters)")

#Check if the number of filtered words is odd or even
num_filtered_words = len(filtered_words)
#Set condition for even number
if num_filtered_words % 2 == 0:
    print(f"The number of filtered words is even ({num_filtered_words})")
#Set condition for odd number
else:
    print(f"The number of filtered words is odd ({num_filtered_words})")