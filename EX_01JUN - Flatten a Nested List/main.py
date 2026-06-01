#Enter the number of lists
num_lists = int(input("Enter number of lists: "))
#Create empty list to hold the other lists
big_list = []
#Loop through the number of lists
for i in range(num_lists):
    #Enter number of elements in inner list
    list_elements = int(input(f"Enter number of elements for list {i + 1}: "))
    #Create empty list to hold the elements of the inner list
    small_list = []
    #Loop through the number of elements in the list
    for j in range(list_elements):
            #Enter each element
            element = int(input(f"Enter element {j + 1}: "))
            #Add each element to the list
            small_list.append(element)
    #Add each inner list to the outer list
    big_list.append(small_list)
#Print the big list
print(f"The list of lists is: {big_list}")

#Create empty list to hold the odd elements
filtered_list_odd = []
#Create empty list to hold the even elements
filtered_list_even = []
#Loop through the list of lists
for sublist in big_list:
    #Loop through each sublist
    for element in sublist:
        #Set condition for identifying the odd elements
        if element % 2 != 0:
            #Add the odd element to the filtered list
            filtered_list_odd.append(element)
        #Set condition for identifying the even elements
        else:
            #Add the even element to the filtered list
            filtered_list_even.append(element)

#Print the filtered lists
print(f"The odd elements are: {filtered_list_odd}")
print(f"The even elements are: {filtered_list_even}")