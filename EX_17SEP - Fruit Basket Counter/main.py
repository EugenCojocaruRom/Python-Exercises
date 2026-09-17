#Print header and separator
print("<-- Fruit Basket Counter -->")
print("----------------------------")

#Have a list of fruits
basket = ["apple", "banana", "apple", "mango", "banana", "apple", "kiwi", "mango", "apple"]

#Print header
print("<-- List of Fruits in the Basket -->")
#Print a list of numbered fruits
for i, item in enumerate(basket, start = 1):
    print(f"{i}. {item}")

#Print header
print("\n<-- Long Name Fruits -->")
long_name_fruits = [fruit for fruit in basket if len(fruit) > 4]
#Print a list of numbered fruits
for i, item in enumerate(long_name_fruits, start = 1):
    print(f"{i}. {item}")

#Build dictionary for storing the count for each fruit
fruit_count = {}
#Loop over the items of the basket list
for fruit in basket:
    #Check if the item is already in the dictionary
    if fruit in fruit_count:
        #Increase the count if the item is already in the dictionary
        fruit_count[fruit] += 1
    else:
        #Set the count to 1 if the item is not already in the dictionary
        fruit_count[fruit] = 1

#Print header
print("\n<-- LEADERBOARD -->")
#Sort the dictionary by fruit count, descending, and print as a leaderboard
sorted_fruits = sorted(fruit_count.items(), key = lambda x: x[1], reverse = True)
for rank, (fruit, count) in enumerate(sorted_fruits, start = 1):
    if count == 1:
        print(f" {rank}. {fruit} - {count} piece")
    else:
        print(f" {rank}. {fruit} - {count} pieces")