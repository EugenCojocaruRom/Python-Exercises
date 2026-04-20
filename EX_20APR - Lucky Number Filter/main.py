#Create empty list
numbers = []
#Prompt user to enter the number of elements in the list
number = input("Enter the number of elements: ")
#Enter the individual elements
for i in range(int(number)):
    #Validate that the user enters a correct value
    while True:
        try:
           #Declare variable and read it from the console (as entered by the user)
           num = int(input(f"Enter number {i + 1}: "))
           # Add the number to the list
           numbers.append(num)
           #Exit the while loop and move to the next number
           break
        except ValueError:
           #Print error message
           print("This is not a valid number. Please try again.")
#Print the list
print(f"The numbers list is: {numbers}")
#Filter the list to include only numbers that are divisible by 3 or end with the digit 7
lucky_numbers = [x for x in numbers if x % 3 == 0 or x % 10 == 7]
#Print the sorted list
print(f"Lucky numbers: {lucky_numbers}")
#Count and print the numbers of elements in the sorted list
print(f"There are {len(lucky_numbers)} lucky numbers.")
#Calculate and print the sum of the lucky numbers
print(f"The sum of the lucky numbers is {sum(lucky_numbers)}")