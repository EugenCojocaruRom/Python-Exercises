from datetime import date

#Declare variable for current year
current_year = date.today().year
#Loop until the user enters a valid value for the birth year
while True:
    try:
        #Prompt user to enter their birth year
        birth_year = int(input("Enter your birth year: "))
        #Set condition for checking that the year entered is correct
        if 1900 < birth_year < current_year:
            break
        else:
            #Print message to enter a valid value
            print("Please enter a valid birth year.")
    except ValueError:
        #Print message to enter a valid value
        print("Incorrect value. Please enter a valid birth year.")

#Calculate age
age = current_year - birth_year
#Print the age
print(f"You are {age} years old (or turning {age} this year).")

#Calculate the year when the user will turn 100
year100 = birth_year + 100
#Print message for the year the user will turn 100
print(f"You will turn 100 in {year100}.")

#Filter the decade birthdays in the 10 - 101 range, in steps of 10
decade_bdays = [decade for decade in range(10, 101, 10) if decade > age]
#Loop through the decade birthdays list
for i, decade in enumerate(decade_bdays):
    #Print message for each decade birthday
    print(f"{i + 1}. You will be {decade} in {birth_year + decade}")