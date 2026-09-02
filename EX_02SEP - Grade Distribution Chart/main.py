#Print header and separator
print("<-- Grade Distribution Chart -->")
print("--------------------------------")

#Create empty list to store the grades
student_grades = []

#Prompt user to enter the number of students
while True:
    try:
        num_students = int(input("Enter the number of students: "))
        if num_students <= 0:
            print("The number of students cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of students
for i in range(num_students):
    #Loop for validating the grade
    while True:
        try:
            #Prompt user to enter the grade
            grade = int(input(f"Enter the grade of student {i + 1}: "))
            #Check that the value is positive and not bigger than 100
            if grade < 0:
                print("The grade must be a positive number. Please try again.")
                continue
            if grade > 100:
                print("The grade cannot be bigger than 100. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add the grade to the student grades list
    student_grades.append(grade)

#Print header
print("\n<-- STUDENTS' GRADES -->")
#Loop over the grades list
for i, grade in enumerate(student_grades, start = 1):
    #Print a numbered list of the grades
    print(f" Grade {i}: {grade} points")

#Print header
print("\n<-- BIG GRADES (at least 60 points) -->")
#Find and print grades bigger than 60
big_grades = [grade for grade in student_grades if grade >= 60]
if len(big_grades) == 0:
    print("No big grades given.")
elif len(big_grades) == 1:
    print(f"There was only 1 big grade:")
else:
    print(f"There were {len(big_grades)} big grades:")
# Print the grades once, regardless of which branch ran above
for grade in big_grades:
    print(f" -> {grade} points")
print(f"\nNumber of students who passed: {len(big_grades)}")
print(f"Number of students who failed: {len(student_grades) - len(big_grades)}")

#Print header
print("\n<-- GRADE DISTRIBUTION CHART -->")
#Define the buckets as (low, high, label) tuples
buckets = [
    (0, 59, "0-59"),
    (60, 69, "60-69"),
    (70, 79, "70-79"),
    (80, 89, "80-89"),
    (90, 100, "90-100")
]
#Loop over each bucket
for low, high, label in buckets:
    #Count how many grades fall within this bucket's range
    count = len([grade for grade in student_grades if low <= grade <= high])
    #Build the bar using string multiplication, and pad the label for alignment
    bar = "#" * count
    print(f"{label:<6}: {bar} ({count})")

#Calculate and print the class average
average = sum(student_grades) / len(student_grades)
print(f"\nClass average: {average:.1f} points")
#Find the bucket(s) with the most students, handling ties
bucket_counts = [(label, len([grade for grade in student_grades if low <= grade <= high])) for low, high, label in buckets]
max_count = max(bucket_counts, key=lambda x: x[1])[1]
top_buckets = [label for label, count in bucket_counts if count == max_count]
#Set condition for printing the appropriate message
if len(top_buckets) == 1:
    print(f"The bucket with the most students is {top_buckets[0]} ({max_count} students).")
else:
    print(f"There's a tie for the most students between {', '.join(top_buckets)} ({max_count} students each).")