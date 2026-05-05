#Prompt user to enter the number
number = int(input("Enter a number: "))
#Loop through the provided value
for n in range(1, number + 1):
    #Inside this loop --> loop from 1 to n + 1
    for i in range(1, n + 1):
        #Print each number followed by space
        print(i, end=" ")
    #Print empty space to move to the next line
    print()

#Filter the even numbers
even_nums = [x for x in range(1, number + 1) if x % 2 == 0]
#Print the even numbers
print(f"Even numbers on last line: {even_nums}")

#Filter the odd numbers
odd_nums = [x for x in range(1, number + 1) if x % 2 != 0]
#Print the odd numbers
print(f"Odd numbers on last line: {odd_nums}")