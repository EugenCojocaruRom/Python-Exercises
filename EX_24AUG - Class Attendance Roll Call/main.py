#Print header and separator
print("<-- Class Attendance Roll Call -->")
print("----------------------------------")

#Prompt user to enter a number of students
while True:
    try:
        num_students = int(input("Enter the number of students in the class: "))
        if num_students <= 0:
            print("The number of students cannot be zero or negative. Please try again.")
            continue
        #If the class is already full, skip this student and stop the process
        if num_students > 40:
            print("The class cannot have more than 40 students!")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")

#Create empty list to store the students' names
student_names = []
#Loop over the number of students
for i in range(num_students):
    #Loop for validating a student's name
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
    #Add the student's name to the student names list
    student_names.append(student_name)

#Create dictionary to track running absence counts per student across all days
absence_counts = {name: 0 for name in student_names}
#Prompt user to enter the number of days to check the attendance
days = int(input("Enter the number of days to check the attendance for: "))
#Outer loop over the number of days
for day in range(days):
    print(f"\n<-- DAY {day + 1} ROLL CALL -->")
    for student_name in student_names:
        #Prompt user to enter an attendance status
        while True:
            attendance_status = input(f"Enter the attendance status for {student_name} (Y / N): ").strip().upper()
            if attendance_status != "Y" and attendance_status != "N":
                print("Invalid status. Please enter Y or N.")
                continue
            break
        print(f" {student_name} | {'Present' if attendance_status == 'Y' else 'Absent'}")
        if attendance_status == "N":
            absence_counts[student_name] += 1

#Build leaderboard, sorted by absence count descending
print(f"\n<-- {days}-DAY ABSENCE LEADERBOARD -->")
leaderboard = sorted(absence_counts.items(), key=lambda x: x[1], reverse=True)
for name, count in leaderboard:
    if count == 0:
        continue
    flag = " ⚠️ frequent absence" if count >= 2 else ""
    print(f"{name}: {count} absence(s){flag}")

if all(count == 0 for count in absence_counts.values()):
    print(f"No absences recorded over the {days} days.")

#Overall attendance rate across all students and all days
total_checks = len(student_names) * days
total_absences = sum(absence_counts.values())
overall_attendance_rate = (total_checks - total_absences) / total_checks * 100

print(f"\nOverall attendance rate across {days} days: {overall_attendance_rate:.1f}%")