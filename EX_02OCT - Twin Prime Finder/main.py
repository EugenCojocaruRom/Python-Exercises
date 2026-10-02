#Print header and separator
print("<-- Twin Prime Finder -->")
print("-------------------------")

#Loop for validating the limit of numbers to check
while True:
    try:
        #Prompt user to specify the limit of numbers to check
        limit = int(input("Enter a limit: "))
        #Check that the limit value is positive
        if limit <= 0:
            print("The limit must be bigger than 0. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")

#Define function to check that a number is prime
def is_prime(n):
    #Set condition for n smaller than 2
    if n < 2:
        return False
    #Loop over each value in the interval 2 -> square root of n + 1 (to also cover the last value of the range)
    for i in range(2, int(n ** 0.5) + 1):
        #Set condition for checking if number n is divisible by the value of i
        if n % i == 0:
            return False
    return True

#Filter and print the prime numbers
prime_numbers = [x for x in range(2, limit + 1) if is_prime(x)]
if not prime_numbers:
    print("No prime numbers.")
else:
    print(f"Prime numbers: {', '.join(map(str, prime_numbers))}")

#Find and print the twin pairs of prime numbers
twin_pairs = []
#Loop over the prime numbers list, without the last element so that i + 1 does not go past the end
for i, p in enumerate(prime_numbers[:-1]):
    #Declare variable for the next prime
    next_p = prime_numbers[i + 1]
    #Check if the difference is 2
    if next_p - p == 2:
        #Append the tuple to the twin pairs list
        twin_pairs.append((p, next_p))
#Print the twins list
if not twin_pairs:
    print(f"No twin primes found up to {limit}.")
else:
    print("Twin primes:")
    for i, (p1, p2) in enumerate(twin_pairs, start = 1):
        print(f" {i}. ({p1}, {p2})")

#BONUS: Prime triplets (three primes that fit within a span of 6,
#e.g. (2, 3, 5), (3, 5, 7), (5, 7, 11) or (7, 11, 13))
#Create empty list to store the triplets
triplets = []
#Loop over the primes, without the last 2 elements so that i + 2 does not go past the end
for i, first in enumerate(prime_numbers[:-2]):
    second = prime_numbers[i + 1]
    third = prime_numbers[i + 2]
    if third - first <= 6:
        triplets.append((first, second, third))
#Print the triplets
if not triplets:
    print(f"No triplets found up to {limit}.")
else:
    print("Triplets:")
    for i, (first, second, third) in enumerate(triplets, start = 1):
        print(f" {i}. ({first}, {second}, {third})")

#Print summary
print("\n<-- SUMMARY -->")
print(f"Total primes found: {len(prime_numbers)}")
print(f"Number of twin primes found: {len(twin_pairs)}")
if twin_pairs:
    print(f"Largest pair: {max(twin_pairs)}")
print(f"Number of triplets found: {len(triplets)}")
if triplets:
    print(f"Largest triplet: {max(triplets)}")
