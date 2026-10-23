#Print header and separator
print("<== Student Report Card ==>")
print("---------------------------")

#Have a dictionary containing student names and lists of scores
scores = {
    "Ana": [88, 92, 79],
    "Bogdan": [55, 61, 48],
    "Carmen": [100, 95, 98],
    "Dan": [72, 68, 75],
    "Ilarion": [60, 75, 74],
    "Elena": [],
}

#Create function for calculating the average of all marks
def calculate_average(marks):
    if not marks:
        return 0
    else:
        return round(sum(marks) / len(marks), 1)

#Create function for assigning a letter to an average
def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

#Create function for building the report card
def build_report_card(all_scores):
    #Create dictionary to store the report cards (names and grades)
    report_cards = {}
    #Loop over the names and marks in the scores dictionary
    for name, marks in all_scores.items():
        average = calculate_average(marks)
        grade = letter_grade(average)
        report_cards[name] = {"average": average, "grade": grade}
    return report_cards

print()
#Print all students with their averages
for name, marks in scores.items():
    print(f"{name}: {calculate_average(marks)}")

#Declare variable for the report and call the build_report_card function
report = build_report_card(scores)

print("\n== Student Ranking ==")
#Sort the students by average
ranked = sorted(report.items(), key=lambda item: item[1]["average"], reverse=True)
#Loop over the ranked list and print the report
for position, (name, info) in enumerate(ranked, start = 1):
    print(f" {position}. {name} - {info['average']} ({info['grade']})")

#Calculate and print the class average (students with no marks are ignored)
averages = [calculate_average(marks) for name, marks in scores.items() if marks]
class_average = calculate_average(averages)
print(f"  -> Class average: {class_average}")

#Loop for validating the value entered by the user
while True:
    try:
        #Prompt user to enter the average value to check
        average_check = float(input("\nEnter an average to check: "))
        if average_check < 0:
            print("The value cannot be negative. Please try again.")
            continue
        if average_check > 100:
            print("The value cannot exceed 100. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")

#Sort the students who passed
passed = [name for name, info in report.items()
          if info["average"] >= average_check and info["grade"] != "F"]
if not passed:
    print("No students match.")
elif len(passed) == 1:
    print(f"Only 1 student with an average over {average_check}: {passed[0]}")
else:
    print(f"The following students have averages over {average_check}: {', '.join(passed)}")

#Create dictionary for storing the number of students per grade
grade_counts = {}
for info in report.values():
    grade = info["grade"]
    grade_counts[grade] = grade_counts.get(grade, 0) + 1
#Loop over the ABCDF string
print("\n== Grade Counts ==")
for letter in "ABCDF":
    print(f" {letter}: {grade_counts.get(letter, 0)}")