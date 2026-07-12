#Define function for formatting the tutor assignments
def format_tutor_assignments(student_records, tutor_profiles):
    #Create list containing the header and a separator
    report_lines = ["TUTOR ASSIGNMENTS", "=================="]

    #Extract the list of tutors from the dictionary
    tutors_list = tutor_profiles.get("tutors", [])
    #Loop through the student records list
    for record in student_records:
        try:
            student_id, name, age_str, subject, progress = record.split(":")
            age = int(age_str)
        except ValueError:
            continue
        matched_tutor_initials = "UNASSIGNED"

        #Iterate through the list of tutor dictionaries
        for tutor in tutors_list:
            tutor_name = tutor.get("name", "")
            subjects = tutor.get("subjects", [])
            age_groups = tutor.get("age_groups", [])  # e.g., [13, 14, 15]
            #Check compatibility (direct subject match and student age in the allowed list)
            if subject in subjects and age in age_groups:
                name_parts = tutor_name.split()
                matched_tutor_initials = "".join([part[0].upper() for part in name_parts if part])
                break
        report_lines.append(f"{matched_tutor_initials} - {name} ({age}) - {subject} - {progress}")

    return "\n".join(report_lines)

#Sample data
student_records = [
    "001:Alice Smith:14:Math:75%",
    "002:Bob Jones:10:Science:40%",
    "003:Charlie Brown:25:Math:90%"
]
tutor_profiles = {
    "T1": {
        "name": "John Doe",
        "subjects": ["Math", "Physics"],
        "age_groups": ["teens", "adults"]
    },
    "T2": {
        "name": "Sarah Jane",
        "subjects": ["Science"],
        "age_groups": ["kids"]
    }
}
#Run the function
print(format_tutor_assignments(student_records, tutor_profiles))