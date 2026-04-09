#Set initial number
secret = 7
#Set number of attempts
attempts = 5
#Loop through number of attempts
for i in range(attempts):
    #Prompt user to enter a number
    guess = int(input("Guess the number (between 1 and 10): "))
    #Set rule for guessed number lower than secret number
    if guess < secret:
        #Print message
        print("Too low! Try again.")
    #Set rule for guessed number bigger than secret number
    elif guess > secret:
        #Print message
        print("Too high! Try again.")
    #Set rule for guessed number equal to secret number
    else:
        #Print message
        print("Correct! You got it!")
        #Exit the loop when the user guesses the number
        break
#Set condition for running out of attempts
else:
    #Print message and the secret number
    print(f"No more attempts left. The secret number was {secret}")