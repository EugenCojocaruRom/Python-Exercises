EX\_12JUL - Format Tutoring Assignment Report

Write a function format\_tutor\_assignments that takes student\_records and tutor\_profiles and returns a formatted assignment report.



The function processes student data, matches them with appropriate tutors based on subject and age group, and generates a comprehensive report showing all assignments.



Logic:



&#x20;   Extract student information from formatted records using substring operations

&#x20;   Match students to tutors based on subject expertise and age group compatibility

&#x20;   Generate tutor initials from full names

&#x20;   Format the final report with proper alignment and progress indicators



Parameters:



&#x20;   student\_records (list): List of formatted student strings in format "ID:Name:Age:Subject:Progress"

&#x20;   tutor\_profiles (dict): Dictionary with tutor data including name, subjects, and age groups



Returns: Formatted assignment report string. 

&#x09;Format: TUTOR ASSIGNMENTS ================== \[Tutor Initials] - \[Student Name] (\[Age]) - \[Subject] - \[Progress] \[Tutor Initials] - \[Student Name] (\[Age]) - \[Subject] - \[Progress]

