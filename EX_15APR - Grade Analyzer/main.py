#Have a list of scores
scores = [72, 45, 91, 58, 83, 67, 99, 34, 76, 88]
#Declare variables for min score and max score
min_score = scores[0]
max_score = scores[0]
#Loop through the list
for i in scores:
    #Set condition for finding the min score
    if i < min_score:
        min_score = i
    #Set condition for finding the max score
    if i > max_score:
        max_score = i
#Print max and min score
print('Highest:', max_score, '| Lowest:',min_score)
#Calculate the average of the scores
avg_scores = sum(scores) / len(scores)
#Print the average
print('Average score:', avg_scores)
#Create list with scores that are considered 'passed'
passed_scores = [x for x in scores if x > 60]
#Print passing scores
print('Passed scores:', passed_scores)
#Loop through the scores
for score in scores:
    # Set conditions for displaying the scores and their corresponding grades
    if score >= 90:
        print(f'Score: {score} -> Grade: A')
    elif score >= 80:
        print(f'Score: {score} -> Grade: B')
    elif score >= 70:
        print(f'Score: {score} -> Grade: C')
    elif score >= 60:
        print(f'Score: {score} -> Grade: D')
    else:
        print(f'Score: {score} -> Grade: F')