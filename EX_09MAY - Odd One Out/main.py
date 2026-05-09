#Prompt for number of elements
nums = int(input("How many numbers? "))
#Create empty list to store the numbers
numbers = []
#Loop through the number of elements
for i in range(nums):
    #Prompt to enter each number
    num = int(input(f"Enter number {i + 1}: "))
    #Add the number to the list
    numbers.append(num)
#Print the list
print(f"The numbers are: {numbers}")

#Filter the odd numbers
odd_nums = [x for x in numbers if x % 2 != 0]
#Print the odd numbers
print(f"The odd numbers are: {odd_nums}")
#Print the count of odd numbers
print(f"There are {len(odd_nums)} odd numbers")
#Calculate the sum of the odd numbers
print(f"The sum is: {sum(odd_nums)}")
#Set condition for no odd numbers
if len(odd_nums) == 0:
    print("No odd numbers")
#Set condition for odd numbers
else:
    #Calculate the average of the odd numbers
    avg_odd = sum(odd_nums) / len(odd_nums)
    print(f"The average is: {round(avg_odd, 2)}")
