#import the 'random' function
import random

#Loop until a correct value is entered
while True:
    #Prompt user to enter the amount of random numbers
    nums = int(input("How many numbers? (max. 100) "))
    #Set condition for value positive and <= 100
    if 1 <= nums <= 100:
        #Exit the loop
        break
    #Set condition for value > 100
    else:
        #Print warning message
        print("Please enter a number between 1 and 100!")

#Create the list of random numbers
random_nums = random.sample(range(1, 101), nums)
#Print the list of numbers
print(f"All numbers: {random_nums}")

#Filter the even numbers
even_numbers = [n for n in random_nums if n % 2 == 0]
#Print the numbers
print(f"Even numbers found: {even_numbers}")

#Loop through the even numbers and assign 'small' / 'big' to each of them
for num in even_numbers:
    #Set condition for small numbers
    if num <= 50:
        print(f"{num} -> small")
    #Set condition for big numbers
    else:
        print(f"{num} -> big")

#Set condition for even numbers - in case of empty list
if even_numbers:
    #Find the biggest even number
    biggest_even = max(even_numbers)
    #Print the number
    print(f"Biggest even number: {biggest_even}")
#Set condition for the case when there might not be any even numbers
else:
    print("There are no even numbers.")

#Filter the odd numbers - in case of empty list
odd_numbers = [n for n in random_nums if n % 2 != 0]
#Set condition for odd numbers
if odd_numbers:
    #Find the biggest odd number
    biggest_odd = max(odd_numbers)
    #Print the number
    print(f"Biggest odd number: {biggest_odd}")
#Set condition for the case when there might not be any odd numbers
else:
    print("There are no odd numbers.")