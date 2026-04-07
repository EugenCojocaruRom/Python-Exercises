#Prompt number of scores
num_scores = int(input('Enter number of scores: '))
#Loop through number of scores
for i in range(num_scores):
    #Prompt for entering each score individually
    score = int(input(f'Enter score {i + 1}: '))
    #Set conditions for displaying the scores and their corresponding grades
    if score >= 90:
        print('Score:', score, '-> Grade: A')
    elif score >= 80:
        print('Score:', score, '-> Grade: B')
    elif score >= 70:
        print('Score:', score, '-> Grade: C')
    elif score >= 60:
        print('Score:', score, '-> Grade: D')
    else:
        print('Score:', score, '-> Grade: F')