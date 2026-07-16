##Print header and separator
print("<-- FITNESS CLASS SIGNUP TRACKER -->")
print("------------------------------------")

#Prompt user to enter the number of fitness classes
num_classes = int(input("Enter the number of classes: "))
#Create empty dictionary to hold the names of the classes and the number of spots for each
classes = {}
count = 0
#Loop through the number of classes
while count < num_classes:
    #Prompt user to enter the name of the class
    class_name = input(f"Enter the name of the class: ").capitalize()
    #Prompt user to enter the number of spots for the class
    num_spots = int(input(f"Enter the number of spots for the {class_name} class: "))
    #Set condition for class name already in the dictionary
    if class_name in classes:
        #Print warning message
        print(f'Class "{class_name}" already exists. Please enter another one.')
    else:
        #Add the class name and the number of spots to the dictionary
        classes[class_name] = num_spots
        count += 1

#Create empty list to hold the names of the people signing up and the class they sign up for
signups = []
#Prompt user to enter the number of people that will sign up
num_signups = int(input("\nEnter the number of signups: "))
#Loop through the number of signups
for i in range(num_signups):
    #Prompt user to enter the name of the signup
    signup_name = input(f"Enter the name of signup {i + 1}: ").title()
    #Check that the class name is correct
    while True:
        #Prompt user to enter the name of the class
        signup_class = input(f"Which class will {signup_name} sign up for? ").capitalize()
        #Set condition for class name found in the classes dictionary
        if signup_class in classes:
            #Exit the loop
            break
        else:
            #Print warning message
            print(f'Class "{signup_class}" does not exist. Please enter a valid class.')
    #Add signup and class to list as tuple
    signups.append((signup_name, signup_class))

#Print header
print("\n<-- Class Summary -->")
#Loop through the classes items
for class_name, capacity in classes.items():
    print(f"{class_name} (capacity {capacity}):")
    #Filter signups down to just this class
    class_signups = [name for name, cls in signups if cls == class_name]
    if not class_signups:
        print("  No sign-ups yet.")
    else:
        #Slice the class capacity into confirmed vs waitlisted
        confirmed = class_signups[:capacity]
        waitlisted = class_signups[capacity:]
        print("  Confirmed:")
        for index, name in enumerate(confirmed, start = 1):
            print(f"    {index}. {name}")
        if waitlisted:
            print("  Waitlisted:")
            for index, name in enumerate(waitlisted, start = 1):
                print(f"    {index}. {name}")
    #Print blank line between classes
    print()

#Create empty lists for the full classes and for the classes with open spots
full_classes = []
open_classes = []
#Loop through the classes items
for class_name, capacity in classes.items():
    #Count the signups
    signups_present = len([name for name, cls in signups if cls == class_name])
    #Set condition for the number of signups bigger or equal to the class capacity
    if signups_present >= capacity:
        #Add the name of the full class to the list
        full_classes.append(class_name)
    #Set condition for the number of signups smaller than the class capacity
    else:
        #Add the name of the class with open spots to the list
        open_classes.append(class_name)
#Print the full and incomplete classes
print(f"Full classes: {len(full_classes)}")
print(f"Classes with open spots: {len(open_classes)}")