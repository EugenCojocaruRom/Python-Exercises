#Prompt user for number of elements
nums = int(input("How many numbers? "))
#Declare empty list to store the numbers
nums_list = []
#Loop through the number of elements
for i in range(nums):
    #Enter each number
    number = int(input(f"Enter number {i + 1}: "))
    #Add the number to the list
    nums_list.append(number)
#Print the list
print(f"The complete number list is: {nums_list}")

#Filter the even numbers
even_nums = [x for x in nums_list if x % 2 == 0]
#Print the even numbers
print(f"Even numbers: {even_nums}")
#Filter the odd numbers
odd_nums = [x for x in nums_list if x % 2 == 1]
#Print the odd numbers
print(f"Odd numbers: {odd_nums}")


#Declare variable for sum of even numbers
sum_even_nums = 0
#Loop through the even numbers list
for n in even_nums:
    #Add each number to the sum at every iteration
    sum_even_nums += n
#Print the sum of even numbers
print(f"Sum of evens: {sum_even_nums}")

#Declare variable for sum of odd numbers
sum_odd_nums = 0
#Loop through the even numbers list
for n in odd_nums:
    #Add each number to the sum at every iteration
    sum_odd_nums += n

#Set condition for the case when there are odd numbers
if len(odd_nums) > 0:
    #Calculate the average of the odd numbers
    avg_odd_nums = sum_odd_nums / len(odd_nums)
    #Print the average of odd numbers
    print(f"Average of odds: {round(avg_odd_nums, 2)}")
#Set condition for the case when there are no odd numbers
else:
    print("No odd numbers")