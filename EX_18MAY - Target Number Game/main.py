import random

#Prompt user to enter the first number of the range
num_a = int(input("Enter the start of the number range: "))
#Prompt user to enter the last number of the range
num_b = int(input("Enter the end of the number range: "))
#Prompt user to specify the numbers of random numbers
rand_num = int(input("How many random numbers to generate? "))
#Create the list of random numbers
num_list = [random.randint(num_a, num_b) for _ in range(rand_num)]
#Print the list
print(f"The numbers list is: {num_list}")

#Randomly generate the target number
target_num = random.randint(num_a, num_b * 2)
#Print the target number
print(f"Target number: {target_num}")


#Print section title
print("Guess to numbers that add up to the target")
#Prompt user to enter the first number
guess1 = int(input("Enter the first number: "))
#Prompt user to enter the second number
guess2 = int(input("Enter the second number: "))

#Check that both guesses are in the list
if (guess1 in num_list and guess2 in num_list
        and guess1 != guess2
        and guess1 + guess2 == target_num):
    #Print success message
    print("Congratulations! You guessed the numbers correctly!")
else:
    #Print failure message
    print("Sorry, you did not guess the numbers!")