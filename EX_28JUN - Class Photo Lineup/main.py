#Print header
print("<-- Class Photo Lineup -->")
#Prompt user to enter the number of students
num_students = int(input("Enter the number of students: "))
#Create empty list to hold the number of students and their heigths
students = []
#Loop through the number of students
for i in range(num_students):
    #Prompt the user to enter the name of the student
    student_name = input(f"Enter the name of student {i + 1}: ").title()
    #Prompt the user to enter the height of the student
    student_height = int(input(f"Enter {student_name}'s height (in cm): "))
    #Add name and height to the list
    students.append((student_name, student_height))

#Sort the students by height (shortest to tallest)
sorted_students = sorted(students, key=lambda student: student[1])
#Print header
print("\nStudents' Heights - shortest -> tallest:")
#Declare variable to calculate the maximum length of the name
max_length = max(len(student_name) for student_name, student_height in students)
#Loop through the sorted list
for student_name, student_height in sorted_students:
    #Print the name and the height
    print(f"{student_name:<{max_length}} - {student_height} cm")

#Print header and separator
print("\n<-- STUDENT LINEUP -->")
print("----------------------")
#Loop through the students list
for i, (student_name, student_height) in enumerate(students, start = 1):
    #print each student and their height
    print(f"{i}. {student_name:<{max_length}} - {student_height} cm")

#Print header
print("\n<-- TALL STUDENTS -->")
#Filter the names of students taller than 150 cm
tall_students = [student_name for student_name, student_height in students if student_height > 150]
#Print the students' names
print(f"The following students are taller than 150 cm: {', '.join(tall_students)}")

#Print header
print("\n<-- AVERAGE HEIGHT -->")
#Calculate the average height
avg_height = sum(student_height for student_name, student_height in students) / len(students)
#Print the average height
print(f"The average height of the student lineup is {avg_height:.1f} cm")

#Print header
print("\n<-- ADD EXTRA STUDENT -->")
#Prompt user to enter the name
extra_student = input("Enter the extra student name: ").title()
#Prompt user to enter the height
extra_student_height = int(input("Enter the extra student height: "))
#Add the new student to the list
students.append((extra_student, extra_student_height))
#Sort the list
sorted_students = sorted(students, key=lambda s: s[1])
#Print the new lineup
print("\n<-- NEW STUDENT LINEUP (sorted) -->")
for student_name, student_height in sorted_students:
    print(f"{student_name:<{max_length}} - {student_height} cm")
