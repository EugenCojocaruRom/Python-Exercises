#Print header and separator
print("<-- Marathon Bib Number Assigner -->")
print("------------------------------------")

#Create empty list to store the runners' names
runners = []
#Prompt user to enter the number of runners registered for the marathon
while True:
    try:
        num_runners = int(input("Enter the number of runners registered for the marathon: "))
        if num_runners <= 0:
            print("The number of runners cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of runners
for i in range(num_runners):
    #Loop for validating the runner's name
    while True:
        #Prompt user to enter the runner's name
        runner_name = input(f"Enter the name of runner {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if runner_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not runner_name.replace(" ", "").replace("-", "").replace("'", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Add the runner name to the runners list
    runners.append(runner_name)

#Print header
print("\n<-- RUNNERS REGISTERED FOR THE MARATHON -->")
#Loop over the runners list
for i, runner_name in enumerate(runners, start = 101):
    #Print the runners and their bib numbers
    print(f" Bib {i}: {runner_name}")

#Print header
print("\n<-- LONG NAME CLUB (name > 5 letters) -->")
#Filter the runners with long names (> 5 letters)
long_name_club = [f"{runner_name} (bib {i})" for i, runner_name in enumerate(runners, start=101) if len(runner_name) > 5]
#Set conditions for displaying the runners with long names
if len(long_name_club) == 0:
    print("There are no runners with long names.")
elif len(long_name_club) == 1:
    print(f"There is only 1 runner with a long name: {long_name_club[0]}")
else:
    print(f"There are {len(long_name_club)} runners with long names: {', '.join(long_name_club)}")
