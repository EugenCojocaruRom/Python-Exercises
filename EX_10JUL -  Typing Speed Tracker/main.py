#Print header
print("<--  Typing Speed Tracker (WPM Calculator) -->")

#Create empty list to hold the WPM
WPM_values = []
#Prompt user to enter the number of typing attempts
attempts = int(input("Enter the number of attempts: "))
#Loop through the number of attempts
for i in range(attempts):
    #Prompt user to type e sentence
    sentence = input(f"Type sentence {i + 1}: ").lower()
    #Calculate the number of words in the sentence
    words = [word for word in sentence.split()]
    #Check that the time value entered is valid
    while True:
        # Prompt user to enter the time it took to type the sentence
        time = int(input("How much time it took to type the sentence (seconds): "))
        if time <= 0:
            print("Incorrect value (must be greater than 0). Please try again.")
        else:
            break
    #Calculate the WPM speed
    wpm = float((len(words) / time) * 60)
    WPM_values.append(wpm)

#Loop through the WPM values
for i, wpm in enumerate(WPM_values, start = 1):
    #Set condition for WPM < 20
    if wpm < 20:
        print(f"Attempt {i}: {wpm:.1f} WPM (Beginner)")
    #Set condition for WPM > 20 and < 150
    elif wpm < 40:
        print(f"Attempt {i}: {wpm:.1f} WPM (Average)")
    #Set condition for WPM > 150
    else:
        print(f"Attempt {i}: {wpm:.1f} WPM (Fast)")

#Find the best WPM
best_wpm = max(WPM_values)
#Find the best WPM value (+1 because attempts are numbered from 1)
best_attempt = WPM_values.index(best_wpm) + 1
#Print the value
print(f"Best WPM: {best_wpm:.1f} (Attempt {best_attempt})")

#Calculate the average WPM
avg_wpm = sum(WPM_values) / len(WPM_values)
#Print the average WPM
print(f"Average WPM: {avg_wpm:.1f} WPM")