#Have a list of random numbers
numbers = [14, 7, 23, 8, 42, 15, 3, 30, 11, 27, 6, 18]
#Create list by using list comprehension to sort the even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
#Print the even numbers
print('Even numbers:', even_numbers)
#Loop through the sorted list of even numbers
for number in even_numbers:
    #Set condition for numbers smaller than 15
    if number < 15:
        print(number, '-> small')
    #Set condition for numbers from 15 upwards
    else:
        print(number, '-> big')
#Initialize variable for sum of even numbers
sum_even_numbers = 0
#Loop through the even numbers list
for number in even_numbers:
    #Add each item of the list to the sum
    sum_even_numbers += number
#Calculate the average of the even numbers from the list
average = sum_even_numbers / len(even_numbers)
#Print the average value
print('Average:', round(average, 2))
#Initialize variable max number as the first number in the even numbers list
max_number = even_numbers[0]
#Loop through the even numbers list
for i in even_numbers:
    if i > max_number:
        max_number = i
print('Max even number:', max_number)
