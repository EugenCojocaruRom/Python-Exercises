#Print header
print("<-- Locker Assignment Checker -->")
#Prompt user to enter the number of lockers
num_lockers = int(input("Enter the number of lockers: "))
#Prompt user to enter a list of student names, comma separated
student_names = [name.strip().title() for name in input("Enter student names (comma separated): ").split(",")]

#Declare variable to calculate the maximum length of the name
max_length = max(len(student_name) for student_name in student_names)
#Check is there are less lockers than students
if num_lockers < len(student_names):
    #Print a warning message
    print("There are fewer lockers than students!")
#Loop through the assign locker list
for locker_number, student in enumerate(student_names, start = 1):
    #Set condition for number of lockers vs number of students
    if locker_number <= num_lockers:
        # Set condition for number of the locker divisible by 3
        if locker_number % 3 == 0:
            #Print message that the student got a window locker
            print(f" - {student:<{max_length}} gets locker {locker_number} (window locker)")
        else:
            #Print the student name and the assigned working locker
            print(f" - {student:<{max_length}} gets locker {locker_number}")
    else:
        #No locker left for this student
        print(f" - {student:<{max_length}} has no locker available")

#Find and print all locker numbers that are multiples of 3 (window lockers)
window_lockers = [str(locker_number) for locker_number in range(1, num_lockers + 1) if locker_number % 3 == 0]
#Print the locker numbers
print(f"Window lockers: {', '.join(window_lockers)}")

#tim, anna belle, john, sam, tom, robert, andy, trisha, pamela martha, bartholomew, james, jonathan

#Prompt user to specify which lockers are broken
broken_lockers = [int(number.strip()) for number in input(f"Enter the numbers of the broken lockers (1-{num_lockers}, comma separated): ").split(",")]
#Filter the good lockers
good_lockers = [locker_number for locker_number in range(1, num_lockers + 1) if locker_number not in broken_lockers]
#Check the number of working lockers vs the number of students
if len(good_lockers) < len(student_names):
    #Print informative message
    print("Not enough working lockers for every student.")
#Assign lockers from the good list to students
for student, locker_number in zip(student_names, good_lockers):
    #Set condition for number of the locker divisible by 3
    if locker_number % 3 == 0:
        # Print message that the student got a window locker
        print(f" - {student:<{max_length}} gets locker {locker_number} (window locker)")
    else:
        #Print the student name and the assigned working locker
        print(f" - {student:<{max_length}} gets locker {locker_number}")
