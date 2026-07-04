#Print header
print("<-- Version Number Comparator -->")

#Prompt user to enter the first number
num_one = input("Enter the first number: ")
#Prompt user to enter the second number
num_two = input("Enter the second number: ")

#Split the string into pieces and turn each piece into an integer
split_num_one = [int(piece) for piece in num_one.split('.')]
split_num_two = [int(piece) for piece in num_two.split('.')]
#Pad the shorter list (if it is the case) with extra zeroes
max_num = max(len(split_num_one), len(split_num_two))
padded_num_one = split_num_one + [0] * (max_num - len(split_num_one))
padded_num_two = split_num_two + [0] * (max_num - len(split_num_two))

#Compare the two lists part by part
versions_equal = True
for i, val_one in enumerate(padded_num_one):
    val_two = padded_num_two[i]
    if val_one > val_two:
        versions_equal = False
        print(f"{num_one} is newer than {num_two}")
        break  #stop the loop here
    elif val_one < val_two:
        versions_equal = False
        print(f"{num_two} is newer than {num_one}")
        break  #stop the loop here
if versions_equal:
    print(f"{num_one} is equal to {num_two}")
