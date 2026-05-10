#Prompt for the number
number = int(input("Enter a number: "))
#Declare counter variable
counter = 0
#Loop for as long as the number is bigger than 1
while number != 1:
    #Print the step
    print(f"{number} -> ", end="")
    #Increment the counter at each iteration
    counter += 1
    #Set condition for even numbers
    if number % 2 == 0:
        number = number // 2
    #Set condition for odd numbers
    else:
        number = number * 3 + 1
#Print the final 1
print(f"1, ({counter} steps)")

#BONUS - range 1 - 100
print("Numbers in the 1 - 100 range")
#Create empty list to store the results
results = []
#Loop from 1 to 101
for start in range(1, 101):
    #Set the number as start
    number = start
    #Declare variable for steps
    steps = 0
    #Loop for as long as the number is bigger than 1
    while number != 1:
        #Increment the counter at each iteration
        steps += 1
        #Set condition for even numbers
        if number % 2 == 0:
            number = number // 2
        #Set condition for odd numbers
        else:
            number = number * 3 + 1
    #Save the number and the number of steps to reach i
    results.append((start, steps))
#Print the "winning" number
print(max(results, key=lambda x: x[1]))

