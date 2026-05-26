import random

#Prompt user to enter the number of seats
num_seats = int(input("Enter number of seats: "))
#Create list of seats
seats = [random.choice(["free", "taken"]) for _ in range(num_seats)]

#Loop through the seats using their indexes and the enumerate function
for i, seat in enumerate(seats):
    #Print each seat with its status
    print(f"Seat {i + 1}: {seat}")
#Filter out the free seats
free_seats = [i + 1 for i, seat in enumerate(seats) if seat == "free"]
print(f"Free seats: {free_seats}")

#Filter the seat pairs
pairs = [(seat, seat + 1) for seat in free_seats if seat + 1 in free_seats]
#Set condition for no adjacent free seats
if len(pairs) == 0:
    #Print message
    print("Sorry, no seats for couples!")
#Set condition if there are adjacent seats
else:
    #Create list to collect the pairs into a string
    adj_pairs = ", ".join(f"({a}, {b})" for a, b in pairs)
    #Print the pairs of adjacent free seats
    print(f"Adjacent free pairs: {adj_pairs}")
    #Print the numbers of free pairs
    print(f"Found {len(pairs)} pair(s) for couples!")