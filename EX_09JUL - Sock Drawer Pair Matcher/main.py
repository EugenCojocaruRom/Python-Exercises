#Print header
print("<-- Sock Drawer Pair Matcher -->")

#Prompt user to enter the sock colors as a comma separated list
sock_colors = input("Enter the sock colors separated by comma: ")

#Declare variable for counting the sock pairs
count = 0
#Create empty dictionary to hold the sock color and the number of pairs
sock_pairs = {}
#Loop through the sock colors list
for color in sock_colors.split(","):
    #Set condition for color in the list
    if color in sock_pairs:
        #Increase the color count
        sock_pairs[color] += 1
    #Set condition for color not in the list
    else:
        #Set color count to 1
        sock_pairs[color] = 1

#Declare variable to store the number of pairs
total_pairs = 0
#Create empty list to hold the leftover colors
leftover_colors = []
#Loop through the sock pairs dictionary
for (color, count) in sock_pairs.items():
    #Increment total_pairs with the number of pairs
    total_pairs += count // 2
    #Check if there are any leftover colors
    if count % 2 == 1:
        #Add the leftover colors to the list
        leftover_colors.append(color)

#Loop through the sock colors list
for i, color in enumerate(sock_colors.split(","), start = 1):
    #Print the sock colors
    print(f"{i}. {color}")
#Sort the odd colors
odd_colors = [color for color, count in sock_pairs.items() if count % 2 == 1]

#Print the number of sock pairs
print(f"Total pairs: {total_pairs}")
#Print the unpaired colors
print(f"Leftover (unpaired) colors: {leftover_colors}")
#Print the odd colors
print(f"Odd colors: {odd_colors}")