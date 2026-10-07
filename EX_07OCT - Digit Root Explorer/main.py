import random

#Print header and separator
print("<-- Digit Root Explorer -->")
print("---------------------------")

#Create function that returns the sum of the digits of a number
def digit_sum(n):
    #Declare variable for storing the sum of the digits of a number and initialize it
    sum_digits = 0
    #Convert the number to a string
    digits = [int(d) for d in str(n)]
    #Add each digit to the sum
    sum_digits += sum(digits)
    #Return the sum of the digits
    return sum_digits
    #return sum(int(d) for d in str(n))

#Create function that keeps calling digit_sum until the result is a single digit + the number of steps
def digital_root(n):
    #Declare variable for storing the number of steps needed to reach the single digit and initialize it
    num_steps = 0
    #Loop for as long as the number had 2 digits or more
    while n >= 10:
        #Make n equal to the value returned by digit_sum()
        n = digit_sum(n)
        #Increment the number of steps by 1
        num_steps += 1
    #Return the number and the number of steps
    return n, num_steps

#Create empty list to store the numbers to explore
numbers = []
#Prompt the user to enter how many numbers to explore
while True:
    try:
        num_numbers = int(input("How many numbers do you want to explore? "))
        if num_numbers <= 0:
            print("The value cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of numbers
for i in range(num_numbers):
    #Generate and add the random numbers to the numbers list
    numbers.append(random.randint(1, 100000))

#Create empty dictionary for storing the roots and the counters
counts = {}
#List the numbers with their digital roots and the number of steps
for i, n in enumerate(numbers, start = 1):
    #Unpack the tuple from the digital root
    root, steps = digital_root(n)
    print(f"{i}. {n} -> root {root} ({steps} steps)")
    #Count how many times this root has appeared
    counts[root] = counts.get(root, 0) + 1

print()
#Build and print a list with the numbers whose digital root is odd
odd_numbers = [n for n in numbers if digital_root(n)[0] % 2 == 1]
if not odd_numbers:
    print("There are no numbers with odd digital roots.")
else:
    print(f"Numbers with an odd root: {', '.join(str(n) for n in odd_numbers)}")

#Find and print which number took the most steps
most_steps_number = max(numbers, key=lambda n: digital_root(n)[1])
steps = digital_root(most_steps_number)[1]
print(f"Most steps: {most_steps_number} ({steps} steps)")

#Print the report header
print("\n<-- DIGIT ROOT REPORT -->")
#Print how many numbers fall into each root
for root in sorted(counts):
    if counts[root] == 1:
        print(f"Root {root}: {counts[root]} number")
    else:
        print(f"Root {root}: {counts[root]} numbers")