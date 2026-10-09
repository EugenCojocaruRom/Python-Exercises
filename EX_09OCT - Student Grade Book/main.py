#Print header and separator
print("<-- Student Grade Book -->")
print("--------------------------")

#Create dictionary with names and grades
grades = {
    "Ana": [9, 10, 8],
    "Mihai": [7, 6, 8, 9],
    "Elena": [10, 10, 9],
    "Radu": [5, 6],
    "Emanuel": [10, 8, 9, 8, 8]
}

#Create function for calculating the average of a list of grades, rounded to 2 decimals
def average(grade_list):
    if not grade_list:
        return 0
    total = 0
    for grade in grade_list:
        total += grade
    return round(total / len(grade_list), 2)

#Create function for adding a grade to a student and creating the student if they don't exist yet
def add_grade(book, name, grade):
    if not 1 <= grade <= 10:
        print(f"Incorrect grade for {name}: {grade}. Use a value from 1 to 10.")
        return
    if name not in book:
        book[name] = [grade]
    else:
        book[name].append(grade)

#Create function for finding the student with the highest average
def best_student(book):
    best_name = None
    best_avg = 0
    for name, marks in book.items():
        avg = average(marks)
        if avg > best_avg:
            best_avg = avg
            best_name = name
    return best_name

#Print all students with averages
for name, marks in grades.items():
    print(f"{name}: {average(marks)}")

#Add a few grades, including one for a new student
add_grade(grades, "Ana", 7)
add_grade(grades, "Maria", 10)
#Sort the students by average
sorted_students = sorted(grades, key=lambda name: average(grades[name]), reverse=True)
#Find the good students (list comprehension)
good_students = [name for name, marks in grades.items() if average(marks) >= 8]

#Print the best student
print(f"Best student: {best_student(grades)}")
#Print the good students (average grades at least 8)
print(f"Students with an average of 8 or more: {', '.join(good_students)}")
#Print the students sorted by average grade
ranking = [f"{name} ({average(grades[name])})" for name in sorted_students]
print(f"Students sorted by average grade: {', '.join(ranking)}")