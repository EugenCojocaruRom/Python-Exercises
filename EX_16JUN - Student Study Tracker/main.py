#Prompt user to enter the number of students
num_students = int(input("Enter the number of students: "))
#Create empty list to store the names, the subjects and the study times
study_log = []
#Loop through the number of students
for i in range(num_students):
    #Prompt user to enter the name of the student
    student_name = input(f"Enter name for student {i + 1}: ").title()
    #Prompt user to enter the subject of study
    subject = input(f"Enter subject: ").title()
    #Prompt user to enter the study time in minutes
    study_time = int(input(f"Enter study time (minutes): "))
    #Add the student, subject and time to the list as tuples
    study_log.append((student_name, subject, study_time))

#Print section title
print("\nStudy Log")
#Loop through the study log list
for i, (student_name, subject, study_time) in enumerate(study_log, start = 1):
    #Print each student
    print(f"{i}. {student_name}: {subject} - {study_time} minutes")

#Print section title
print("\nTotal Study Time Per Student")
#Create empty dictionary to hold the names and the study times
total_minutes = {}
#Loop through the study log
for (student_name, subject, study_time) in study_log:
    #Set condition for the case when the student is already in the dictionary
    if student_name in total_minutes:
        #Add the study time to the already existing study time for that student
        total_minutes[student_name] += study_time
    #Set condition for the case when the student is added for the first time to the dictionary
    else:
        #Add the study time corresponding to the student to the dictionary
        total_minutes[student_name] = study_time
#Loop through the dictionary
for (student_name, study_time) in total_minutes.items():
    #Print the students with their corresponding total study time
    print(f" -> {student_name} has studied for {study_time} minutes.")

#Print section title
print("\nThe following students have had study sessions longer than 40 minutes:")
#Filter the long sessions
long_sessions = [(student_name, study_time) for student_name, subject, study_time in study_log if study_time >= 40]
#Loop through the list
for name, time in long_sessions:
    #Print the names of the students
    print(f" -> {name} - {time} minutes")

#Find the student with the most total study time
max_study_time = max(total_minutes, key = lambda x: total_minutes[x])
#Print section title
print(f"\nThe student with the most total study time is {max_study_time} ({total_minutes[max_study_time]} minutes).")

#Prompt the user to enter a minimum study threshold
min_study_time = int(input("\nEnter the minimum total study time (minutes): "))
#Loop through the total minutes dictionary
for (student_name, study_time) in total_minutes.items():
    if study_time == min_study_time:
        print(f" -> {student_name} has studied for exactly {min_study_time} minutes.")
    elif study_time > min_study_time:
        print(f" -> {student_name} has exceeded the minimum total study time.")
    else:
        print(f" -> {student_name} has not studied enough.")