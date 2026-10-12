#Print header and separator
print("<-- Student Attendance Streak Report -->")
print("----------------------------------------")

#Have list of names and attendance
attendance = {
    "Ana":    ["P", "P", "A", "P", "P"],
    "Bogdan": ["A", "P", "P", "P", "P"],
    "Carmen": ["P", "A", "A", "P", "A"],
    "Dan":    ["P", "P", "P", "P", "P"],
    "Elena":  ["A", "A", "P", "A", "A"],
    "Maria": ["A", "A", "P"],
    "Mihai": ["A", "A", "P", "A", "A"],
    "Tudor": ["P", "A", "P", "P", "A", "A"],
    "Jan": [],
    "Florin": ["A", "X", "P", "A", "P"],
    "Radu": None
}

#Have list of days
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

#Create function for validating the students
def validate_records(name, records):
    if not isinstance(records, list): #Check the data type
        raise ValueError(f"{name}: expected a list, got {type(records).__name__}")
    if len(records) != len(days):
        raise ValueError(f"{name}: expected {len(days)} days, got {len(records)}")
    for day, record in zip(days, records):
        if record not in ("A", "P"):
            raise ValueError(f"{name}: invalid value '{record}' on {day}")

#Create function that takes one student’s list and returns the percentage of days present (e.g. 80.0)
def attendance_rate(records):
    if not records:
        return 0.0
    #Declare variable as counter for 'present' and initialize it
    present = 0
    for record in records:
        if record == "P":
            present += 1
    return (present / len(records)) * 100

#Create function that returns the longest run of consecutive "P" days for one student
def longest_streak(records):
    #Declare variable for current streak and initialize it
    current_streak = 0
    #Declare variable for best streak and initialize it
    best_streak = 0
    #Loop over records
    for record in records:
        if record == "P":
            current_streak += 1
            if current_streak > best_streak:
                best_streak = current_streak
        else:
            current_streak = 0
    return best_streak

#Create empty lists to stor the valid students and the ones with errors
valid_lines = []
errors = []
#Create empty dictionary for valid attendance
valid_attendance = {}
#Loop over the items in the attendance dictionary
for name, records in attendance.items():
    try:
        validate_records(name, records)
        valid_attendance[name] = records
        valid_lines.append(f"{name}: {attendance_rate(records):.1f}% present")
    except ValueError as error:
        errors.append(str(error))
print("Valid students:")
for line in valid_lines:
    print(f" {line}")
print("\nErrors found:")
for message in errors:
    print(f"- {message}")
print(f"\nSummary: {len(valid_lines)} valid, {len(errors)} rejected")

print("\n<-- Attendance Streaks -->")
#Build a report per student
for i, (name, records) in enumerate(valid_attendance.items(), start = 1):
    print(f" {i}. {name}: {attendance_rate(records):.1f}% present. Longest streak: {longest_streak(records)}")

print("\n<-- Presence 100% -->")
#Filter the students with perfect attendance
full_attend = [name for name, records in valid_attendance.items() if attendance_rate(records) >= 100]
if not full_attend:
    print("There are no students with perfect attendance.")
elif len(full_attend) == 1:
    print(f"Only 1 student with perfect attendance: {', '.join(full_attend)}")
else:
    print(f"Students with perfect attendance: {', '.join(full_attend)}")

print("\n<-- Presence <50% -->")
#Create a list of names of students with an attendance rate below 50%
needs_attention = sorted([name for name, records in valid_attendance.items() if attendance_rate(records) < 50])
if not needs_attention:
    print("No student requires special attention.")
elif len(needs_attention) == 1:
    print(f"Only 1 student requires special attention: {', '.join(needs_attention)}")
else:
    print(f"Students requiring special attention: {', '.join(needs_attention)}")

#Build a list of absences per day
absences_per_day = [sum(1 for records in valid_attendance.values() if records[i] == "A") for i in range(len(days))]
#Declare variable for the highest number of absences on any single day
worst_count = max(absences_per_day)
worst_days = [days[i] for i, count in enumerate(absences_per_day) if count == worst_count]
if worst_count == 0:
    print("\nNo absences this week.")
elif len(worst_days) == 1:
    print(f"\nWorst day: {worst_days[0]} ({worst_count} absences)")
else:
    print(f"\nWorst days (tie): {', '.join(worst_days)} ({worst_count} absences each)")

#Create the missing days report
print("\n<-- Missed days -->")
for name, records in valid_attendance.items():
    missed = [day for day, record in zip(days, records) if record == "A"]
    if missed:
        print(f"{name} missed: {', '.join(missed)}")
    else:
        print(f"{name} missed: none")