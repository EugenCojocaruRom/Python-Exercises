#Print header and separator
print("<-- Study Group Formation Assistant -->")
print("---------------------------------------")

#Create empty list to store the students' names and the scores they got
students = []
#Prompt user to enter the number of students
while True:
    try:
        num_students = int(input("Enter the number of students that took the quiz: "))
        if num_students <= 0:
            print("The number of students cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of students
for i in range(num_students):
    #Loop for validating the student's name
    while True:
        #Prompt user to enter the student's name
        student_name = input(f"Enter the name of student {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if student_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not student_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Loop for validating the score obtained at the quiz
    while True:
        try:
            #Prompt user to enter the score
            score = float(input(f"Enter the quiz score obtained by {student_name}: "))
            #Check that the score value is positive
            if score < 0:
                print("The score must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add student name and score to the students list
    students.append((student_name, score))

#Print header
print("\n<-- STUDENTS' QUIZ SCORES -->")
#Loop over the students list
for i, (student_name, score) in enumerate(students, start = 1):
    #Print the student name and score
    print(f" {i}. {student_name} - {score:.0f} points")

#Calculate the class average score
average_score = sum(score for student_name, score in students) / len(students)
print(f"  Class average score: {average_score:.1f} points")

#Print header
print("\n<-- STUDENTS WHO PASSED (> 70 points) -->")
#Find and print all students who passed (score > 70 points)
passed = [(student_name, score) for student_name, score in students if score >= 70]
if len(passed) == 0:
    print("No passing score in this student group.")
elif len(passed) == 1:
    print(f"There was only 1 student who passed:")
else:
    print(f"There were {len(passed)} students who passed:")
# Print the names once, regardless of which branch ran above
for student_name, score in passed:
    print(f" {student_name} - {score:.0f} points")
#Print how many students passed vs. failed
print(f" -> Students passed: {len(passed)}")
print(f" -> Students failed: {len(students) - len(passed)}")

#Find the student(s) with the highest score
print()
top_score = max(students, key=lambda x: x[1])[1]
top_high_scores = [(student_name, score) for student_name, score in students if score == top_score]
if len(top_high_scores) == 1:
    top_student, top_points = top_high_scores[0]
    print(f"Top student: {top_student} ({top_points:.0f} points)")
else:
    names = ', '.join(name for name, points in top_high_scores)
    print(f"Top students ({top_score:.0f} points): {names}")
