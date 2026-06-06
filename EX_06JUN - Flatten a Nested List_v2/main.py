#Define function for flattening the lists of lists
def flatten(nested_list):
    #Create empty list for odd numbers
    filtered_odd = []
    #Create empty list for even numbers
    filtered_even = []
    #Loop through the empty list
    for sublist in nested_list:
        #Loop through the sublists
        for num in sublist:
            # Set condition for identifying the odd elements
            if num % 2 != 0:
                # Add the odd element to the filtered list
                filtered_odd.append(num)
            # Set condition for identifying the even elements
            else:
                # Add the even element to the filtered list
                filtered_even.append(num)
    #Return the filtered lists
    return filtered_odd, filtered_even

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
#Print the big lists
print(f"The list of lists is: {big_list}")

#Call the function for both odd and even numbers
odd, even = flatten(big_list)
#Print the filtered lists
print(f"The odd elements are: {odd}")
print(f"The even elements are: {even}")