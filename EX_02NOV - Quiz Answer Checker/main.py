#Print header and separator
print("<== Quiz Answer Checker ==>")
print("---------------------------")

#Have a predefined list of answer keys
answer_key = ["B", "A", "D", "C", "A", "B", "C", "D", "A", "B"]
#Have a predefined list of answers given by students
student_answers = ["B", "A", "c", "C", "A", "d", "C", "D", "b", "B"]

#Loop through the student answers list and compare with the answer keys
for i, (answer, key) in enumerate(zip(student_answers, answer_key), 1):
    if answer.upper() == key.upper():
        print(f"Question {i}: {answer.upper()} - Correct")
    else:
        print(f"Question {i}: {answer.upper()} - Wrong (correct answer: {key.upper()})")

#Build a list of the question numbers the student got wrong
wrong_answers = [i for i, (answer, key) in enumerate(zip(student_answers, answer_key), 1) if answer != key]
#Print the number of wrong answers
if not wrong_answers:
    message = "No wrong answers"
else:
    message = f"{wrong_answers}"

#Calculate and print the number of correct answers
correct_answers = len(answer_key) - len(wrong_answers)
if correct_answers == 0:
    print("No questions answered correctly.")
elif correct_answers == 1:
    print("Only 1 question with a correct answer.")
else:
    print(f"{correct_answers} questions answered correctly.")

#Calculate the percentage of correct answers
percentage = correct_answers * 100 / len(answer_key)
#Set conditions for pass / fail
if percentage >= 60:
    result = "Pass"
else:
    result = "Fail"

#Print summary
print("\n== SUMMARY ==")
print(f"Score: {correct_answers}/{len(answer_key)}")
print(f"Percentage: {percentage:.1f}%")
print(f"Wrong questions: {message}")
print(f"Result: {result}")