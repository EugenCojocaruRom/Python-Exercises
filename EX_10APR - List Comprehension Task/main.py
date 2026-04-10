#Prompt user to enter the number of words in the list
word_count = int(input('Enter the number of words in the list: '))
#Add each word entered by the user to the list
words = [input(f'Enter word {i + 1}: ') for i in range(word_count)]
#Sort and add to the new list the words longer than 4 characters
newlist = [x for x in words if len(x) > 4]
#Print the sorted list
print('Sorted list:', newlist)