#Print header
print("<-- Word Frequency Counter -->")

#Prompt user to enter the text to analyze
user_text = input("Enter your text: ").lower()
#Split the text into separate words
split_text = user_text.split()
#Strip the text of any punctuation
clean_text = [word.strip('.,!?"') for word in split_text]

#Create a list of words to filter out
stop_words = ["the", "of", "it", "was", "a", "an", "is", "in", "on", "and", "to"]
#Filter the words to exclude the stop words
filtered_text = [word for word in clean_text if word not in stop_words]
#Create empty dictionary to hold the words and their counts
word_counts = {}
#Loop through the clean text
for word in filtered_text:
    #Set condition for word not in the dictionary
    if word not in word_counts:
        #Set the count to 1
        word_counts[word] = 1
    #Set condition for word already in the dictionary
    else:
        #Increase the count by 1
        word_counts[word] += 1

#Sort the words by the count value
sorted_words = sorted(word_counts.items(), key = lambda x: x[1], reverse = True)
#Loop through the sorted words
for i, (word, count) in enumerate(sorted_words, start = 1):
    #Set condition for words that appear only 1 time
    if count == 1:
        print(f"{i}. {word} -> {count} time")
    else:
        #Print the words and their counts
        print(f"{i}. {word} -> {count} times")


# "It was the best of times, it was the worst of times,
# it was the age of wisdom, it was the age of foolishness,
# it was the epoch of belief, it was the epoch of incredulity,
# it was the season of light, it was the season of darkness,
# it was the spring of hope, it was the winter of despair."