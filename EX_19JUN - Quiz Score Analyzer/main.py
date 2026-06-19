#Prompt user to enter the number of students
num_students = int(input("How many students have taken the quiz? "))
#Create empty list to hold the student names and their quiz scores
students = []
#Loop through the number of students
for i in range(num_students):
    #Prompt user to enter the name of the student
    student_name = input(f"Enter name for student {i + 1}: ").title()
    while True:
        try:
            #Prompt user to enter the score
            student_score = int(input(f"Enter score for student {i + 1}: "))
            #Add a check for scores outside the valid range
            if student_score < 0 or student_score > 100:
                print("Please enter a number between 0 and 100.")
                continue
            #Valid input — exit the while loop
            break
        except ValueError:
            print("Please enter a number between 0 and 100.")
    #Add name and score to the list as tuples
    students.append((student_name, student_score))

#Print section title
print("\nThe following students have taken the quiz:")
#Loop through the students list
for i, (name, score) in enumerate(students, start = 1):
    #Print each student and the score
    print(f"{i}. {name}: {score}/100")

#Print section title
print("\n<-- SCORE LEADERBOARD -->")
#Create a list to hold only the scores
score_only = [score for name, score in students]
#Calculate the average score
avg_score = sum(score_only) / len(score_only)
#Print the average score
print(f"The average score is {avg_score:.2f} points.")
#Loop through the students list
for name, score in students:
    #Set condition for score above average
    if score > avg_score:
        #Print message with the difference in points
        print(f" -> {name} is above the average score by {(score - avg_score):.2f} points.")
    #Set condition for score below average
    elif score < avg_score:
        #Print message with the difference in points
        print(f" -> {name} is below the average score by {(avg_score - score):.2f} points.")
    #Set condition for score equal to average
    else:
        #Print informative message
        print(f" -> {name} has scored as many points as the class average.")

#Find the student with the maximum score
top_name, top_score = max(students, key = lambda x: x[1])
#Print the student with the highest score
print(f"Top scorer: {top_name} with {top_score}/100")

#Print section title
print(f"\n<-- Students who scored above average ({avg_score:.2f} points) -->")
#Filter the students with scores bigger than the average
best_students = [(name, score) for name, score in students if score > avg_score]
#Loop through the best students list
for name, score in best_students:
    #Print each name and the corresponding score
    print(f" -> {name}, with {score} points.")

#Create a function to assign letter grades based on the score
def get_grade(score):
    #Set conditions for the letter grades to be assigned based on the score
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#Print section title
print("\n<-- Ranking by score -->")
#Sort the students from the highest score to the lowest
high_to_low = sorted(students, key = lambda x: x[1], reverse = True)
#Loop through the high to low list
for i, (name, score) in enumerate(high_to_low, start = 1):
    #Call the get_grade function
    grade = get_grade(score)
    #Print the students and the scores
    print(f'{i}. {name} - {score} points ("{grade}")')
