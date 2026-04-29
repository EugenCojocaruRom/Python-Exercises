#Set number of names
num_names = int(input("Enter the number of names: "))
#Define empty list to store the names
names_list = []
#Loop through the number of names
for i in range(num_names):
    #Prompt user to enter each name
    name = input(f"Enter name {i + 1}: ")
    #Add each name to the list
    names_list.append(name)
#Print the names list
print(f"The names are: {names_list}")

#Declare empty list to hold the unique names
unique_names = []
#Loop through the names list, one name at a time
for i in names_list:
    #Declare variable to store name in lowercase
    name_lower = i.lower()
    #Set condition for the names that are not in the unique names list
    if name_lower not in unique_names:
        #Add the name to the unique names list
        unique_names.append(name_lower)
print(f"The unique names are: {unique_names}")

#Capitalize the names in the unique names list and sort the alphabetically
cap_names = sorted([name.capitalize() for name in unique_names])
#Print the capitalized names
print(f"The capitalized and ordered names are: {cap_names}")

#Create list for enumerating the names, starting at 1
list_names = enumerate(cap_names, start = 1)
#Loop through the names in the list
for number, name in list_names:
    #Print number and name
    print(f"{number}. {name}")
