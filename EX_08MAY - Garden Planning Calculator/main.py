#Read three integers from the user
num1 = int(input("Enter number 1: "))  #for finding the closest prime (for plot assignments)
num2 = int(input("Enter number 2: "))  #for calculating the sum-product of its digits
num3 = int(input("Enter number 3: "))  #for checking whether it falls in the ideal planting range

#Helper function -> to check if a given number is prime
def is_prime(n):
    #Set condition for numbers less than 2 (0, 1, negatives) - never prime
    if n < 2:
        return False
    #Check divisors up to the square root of n (math shortcut
    for i in range(2, int(n**0.5) + 1):
        #If n divides evenly by i, it has a factor -> not prime
        if n % i == 0:
            return False
    #If no factors are found -> n is prime
    return True

#Find the closest prime to num1
def closest_prime(n):
    #Set condition for the case when num1 is prime
    if is_prime(n):
        return n
    #Start checking one step away from n in both directions
    offset = 1
    #Keep expanding the search until a prime is found
    while True:
        #Check the number below n at current distance
        if is_prime(n - offset):
            #Return it if prime
            return n - offset
            #Check the number above n at current distance
        if is_prime(n + offset):
            # Return it if prime
            return n + offset
        #No prime found at this distance -> widen the search
        offset += 1
#Call the function and store the result
closest_prime = closest_prime(num1)

#Calculate the sum-product of num2's digits
#Sum up all the individual digits
digit_sum = sum(
    # Convert each character back to an integer
    int(d)
    # abs() handles negative numbers; str() allows looping over each digit
    for d in str(abs(num2))
)
#Multiply the digit sum by itself (square it)
sum_product = digit_sum * digit_sum

#Check if num3 is in the ideal planting range (10 to 20 inclusive)
in_range = "YES" if 10 <= num3 <= 20 else "NO"

#Print each result on a separate line
print(f"Closest prime: {closest_prime}")   #Result 1: closest prime to num1
print(f"Squared digit sum: {sum_product}")   #Result 2: squared digit sum of num2
print(f"Within planting range: {in_range}")  #Result 3: whether num3 is in the planting range