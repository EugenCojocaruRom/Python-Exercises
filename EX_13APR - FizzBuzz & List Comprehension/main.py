#Declare variable and cast the value entered by the user to int
number = int(input('Enter a number: '))
#Loop through the range from 1 to number + 1 to also include the number itself
for i in range(1, number + 1):
    #Set condition for number divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    #Set condition for number divisible by 3
    elif i % 3 == 0:
        print('Fizz')
    #Set condition for number divisible by 5
    elif i % 5 == 0:
        print('Buzz')
    #For all other numbers, just print the number
    else:
        print(i)
#Filter the non-FizzBuzz numbers using list comprehension
filtered_list = [x for x in range(1, number + 1) if x % 3 != 0 and x % 5 != 0]
#Set variable for sum and calculate the sum of the filtered numbers using the sum() function
sum_x = sum(filtered_list)
#Print the sum
print('Sum of non-FizzBuzz numbers:', sum_x)