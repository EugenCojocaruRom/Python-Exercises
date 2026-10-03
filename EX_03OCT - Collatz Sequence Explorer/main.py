#Print header and separator
print("<-- Collatz Sequence Explorer -->")
print("---------------------------------")

#PART 1: Build the sequence

#Define a function that takes a starting number n
def collatz(n):
    #Start the list with the starting number itself
    sequence = [n]
    #Keep going as long as n is bigger than 1
    while n > 1:
        #Set condition for when n is even
        if n % 2 == 0:
            # ...divide it by 2 (// keeps it an integer)
            n = n // 2
        #Set condition for when n is odd
        else:
            #Multiply by 3 and add 1
            n = n * 3 + 1
        #Add the new value to the list
        sequence.append(n)
    #Return the finished list
    return sequence


#PART 2: Print the senquence with enumerate()

#Get the full sequence for 27 and store it
seq_27 = collatz(27)
#Slice the first 10 items -> use enumerate() for (index, value) pairs
for step, value in enumerate(seq_27[:10]):
    #Print each step
    print(f"Step {step}: {value}")


#PART 3: Stats

#Prompt the user for a starting number
number = int(input("\nEnter a number: "))
#Set condition to continue if the number is a positive integer
if number < 1:
    #Print message to inform the user on what went wrong
    print("Please enter a positive integer.")
#Set condition to calculate the stats
else:
    #Build the sequence once and reuse it
    seq = collatz(number)
    #Print the number of steps, i.e. the length of the list minus 1 (the starting number is not a step)
    print(f"Number of steps: {len(seq) - 1}")
    #Use max() to find the highest value in the list
    print(f"Highest value reached: {max(seq)}")


#PART 4: Compare many numbers (list comprehension)

#Build a list of (start, steps) pairs for every start from 1 to 30
#range(1, 31) stops at 30 because the end value is excluded
pairs = [(start, len(collatz(start)) - 1) for start in range(1, 31)]
#Find the pair with the most steps; key=... tells max() to compare the second item (steps)
best_start, best_steps = max(pairs, key=lambda pair: pair[1])
#Print the winner
print(f"\nMost steps: {best_start} takes {best_steps} steps")
#Build a list containing only the pairs with fewer than 10 steps
short_ones = [pair for pair in pairs if pair[1] < 10]
#Print the numbers that qualified
print(f"Numbers with fewer than 10 steps: {len(short_ones)}")


#BONUS: Single line with arrows

#Turn each number into a string and then join them with " -> "
arrow_line = " -> ".join(str(x) for x in collatz(best_start))
#Print the final one-line sequence
print(f"\nSequence for {best_start}:\n{arrow_line}")