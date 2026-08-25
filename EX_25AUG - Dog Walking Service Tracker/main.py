#Print header and separator
print("<-- Dog Walking Service Tracker -->")
print("-----------------------------------")

#Create empty list to store the dogs' names and the walk duration
dog_walks = []
#Prompt user to enter the number of walks
while True:
    try:
        num_walks = int(input("Enter the number of walks for the day: "))
        if num_walks <= 0:
            print("The number of walks cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of walks
for i in range(num_walks):
    #Loop for validating the dog's name
    while True:
        #Prompt user to enter the dog's name
        dog_name = input(f"Enter the name of dog {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if dog_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not dog_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a walk duration in minutes
    while True:
        try:
            duration = int(input(f"Enter walk duration for {dog_name}: "))
            #Check that the duration value is positive
            if duration <= 0:
                print("The duration must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add dog name and duration to the dog walks list
    dog_walks.append((dog_name, duration))

#Print header
print("\n<-- DOG WALKS FOR TODAY -->")
#Loop over the dog walks list
for i, (dog_name, duration) in enumerate(dog_walks, start = 1):
    #Print the dog name and duration
    print(f" Walk #{i} | Dog name: {dog_name} -> Duration: {duration} minutes")

#Calculate the total walk time for all dogs
total_walk_time = sum(duration for dog_name, duration in dog_walks)
print(f"  Total walk time for all dogs: {total_walk_time} minutes")

#Print header
print("\n<-- LONG WALKS (> 40 minutes) -->")
#Find and print all walks longer than 40 minutes
long_walks = [(dog_name, duration) for dog_name, duration in dog_walks if duration > 40]
if len(long_walks) == 0:
    print("No walk longer than 40 minutes found!")
elif len(long_walks) == 1:
    print(f"There was only 1 long walk:")
    for dog_name, duration in long_walks:
        print(f" {dog_name} - {duration} minutes")
else:
    print(f"There were {len(long_walks)} long walks:")
    for dog_name, duration in long_walks:
        print(f" {dog_name} - {duration} minutes")

#Create empty dictionary for the total walk duration per dog
duration_per_dog = {}
#Loop over the dog walks list
for dog_name, duration in dog_walks:
    #Set condition for dog name already in the dictionary
    if dog_name in duration_per_dog:
        #Increment the duration by the corresponding value
        duration_per_dog[dog_name] += duration
    #Set condition for dog name not in the dictionary
    else:
        #Set the duration as the corresponding value
        duration_per_dog[dog_name] = duration
#Sort and print the dog names ordered by total duration
sorted_walks = sorted(duration_per_dog.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Walk Duration per Dog -->")
for i, (dog_name, total) in enumerate(sorted_walks, start = 1):
    print(f" {i}. {dog_name} - {total} minutes")