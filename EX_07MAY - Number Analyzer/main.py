#Prompt user for number of elements
num_numbers = int(input("How many numbers? "))
#Create empty list to store the numbers
numbers_list = []
#Loop through the number of elements
for i in range(num_numbers):
    #Enter each number
    number = int(input(f"Enter number {i + 1}: "))
    #Add the number to the list
    numbers_list.append(number)
#Print the numbers list
print(f"Numbers entered: {numbers_list}")

#Find the largest number
max_number = max(numbers_list)
#Print the number
print(f"Max number: {max_number}")

#Find the smallest number
min_number = min(numbers_list)
#Print the number
print(f"Min number: {min_number}")

#Calculate the sum of all numbers
total_sum = sum(numbers_list)
#Print sum of all numbers
print(f"Total sum: {total_sum}")

#Calculate the average
avg_numbers = total_sum / num_numbers
#Print the value
print(f"Average: {avg_numbers}")

#Filter the numbers that are above the average
above_average = [x for x in numbers_list if x > avg_numbers]
#Print the number(s)
print(f"Numbers above average: {above_average}")