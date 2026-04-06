#Prompt user to enter a number
number = int(input("Enter a number: "))
#Check that the number entered is bigger than 2
if number < 2:
    #Print message
    print(number, 'is not a prime number')
#If the number is bigger than 2, run the loop
else:
    #Loop from 2 to the value of the number
    for i in range(2, number):
        #Set condition to check if any of the numbers in the range divide the given number evenly
        if number % i == 0:
            #Display message
            print(number, 'is not a prime number')
            #End the loop
            break
    #If none of the numbers in the range divide the given number evenly, print message that it is a prime number
    else:
        print(number, 'is a prime number')
