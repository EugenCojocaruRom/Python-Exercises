#Declare empty list
guest_list = []
#Prompt user to enter number of guests
guest_number = int(input("Enter the number of guests: "))
#Loop through the number of guests
for i in range(guest_number):
    #Prompt user to add the name of each guest
    guest_name = input(f"Enter name of guest {i + 1}: ")
    #Add the guest name to the list
    guest_list.append(guest_name)
#Print the guest list
print(f"This is your guest list: {guest_list}")
#Remove any extra spaces from the names
stripped_name = [x.replace(" ", "") for x in guest_list]
#Create cleaned guest list
    #Capitalize each name using title() --> good for names like Mary Jane, Marc Anthony
    #Retain only the names that contain only letters --> isalpha()
cleaned_list = [x.title() for x in stripped_name if x.isalpha()]
#Create a list of unique names by using set() --> set does not allow duplicates
unique_names = list(set(cleaned_list))
#Print the unique names in the cleaned list
print(f"The cleaned guest list is: {unique_names}")