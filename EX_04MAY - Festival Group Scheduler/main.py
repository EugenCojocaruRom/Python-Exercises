#Read the group position; convert to integer
n = int(input())
#Read the delay time in minutes; convert to integer
delay = int(input())
#Read the string of time slots, split it by spaces, convert each part to int and store it in a list
time_slots = list(map(int, input().split()))

    #Finding the nth square-free number
#Declare variable (counter for square-free numbers) and initialize it
count = 0
#Declare variable and initialize it -> for testing the numbers
candidate = 0
#Loop until the nth square-free numbers is found
while count < n:
    #Increment this number to check the next integer
    candidate += 1
    #Set this variable as true by default
    is_square_free = True
    #Check if candidate is divisible by any perfect square > 1
    i = 2
    #Loop for as long as the condition remains true
    while i * i <= candidate:
        #Set condition to check that the candidate is divisible by the current square (i*i)
        if candidate % (i * i) == 0:
            #If divisible, it is not square-free
            is_square_free = False
            #Exit the inner loop
            break
        #Move to the next int
        i += 1
    #Set condition for numbers that are not divisible by a square number
    if is_square_free:
        #Increment the counter
        count += 1
#After the loop finishes, 'candidate' holds the n-th square-free number
square_free_number = candidate

#Print the square-free group number
print(square_free_number)

#Create a new list where 'delay' is added to every original time slot
adjusted_slots = [slot + delay for slot in time_slots]
#Use the * operator to unpack the list and print each adjusted time slot separated by a space
print(*adjusted_slots)