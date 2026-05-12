#Read the three ingredient measurements (in drams)
measurement1 = int(input("Enter measurement 1: "))
measurement2 = int(input("Enter measurement 2: "))
measurement3 = int(input("Enter measurement 3: "))

#Read the performance score
performance = int(input("Enter the performance score (1 - 100): "))

#Check if the measurements form a geometric progression
if measurement1 != 0 and measurement2 * measurement2 == measurement1 * measurement3:
    #Print message
    print("Progression: Geometric")
#Condition for all other cases
else:
    #Print message
    print("Progression: Not geometric")

#Declare variable 'bonus' of type int, initial value 10
bonus = 10
#Set condition for performance score between 80 and 89
if 80 <= performance <= 89:
    #Multiply the bonus by 1.5
    bonus = bonus * 1.5
#Set condition for performance score between 90 and 100
elif 90 <= performance <= 100:
    #Multiply the bonus by 2.0
    bonus = bonus * 2.0
#Set condition for all other cases
else:
    #Keep the bonus as the original one (integer 10)
    bonus = bonus

#Print the bonus
print("Bonus: ", bonus)