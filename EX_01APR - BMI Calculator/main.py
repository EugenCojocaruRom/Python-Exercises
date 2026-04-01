#Display section title
print('<=== BMI Calculator ===>')

#Set variables of type float for weight and height and prompt the user to enter values
weight = float(input('Enter weight: '))
height = float(input('Enter height: '))

#Define function to calculate the BMI
def bmi(weight, height):
    #Set variable for storing the result of the BMI calculation formula
    index = weight / (height * height)
    #Return the resulting value
    return index

#Display section title
print('<=== Result ===>')

#Set a variable to store the value resulting when calling the function
result = bmi(weight, height)

#Display the result formatted to 2 decimals
print(f'BMI: {result:.2f}')

#Display section title
print('<=== Body Type ===>')

#Set conditions for displaying various body types depending on the resulting BMI
if result < 18.5:
    print('Underweight')
elif result < 25:
    print('Normal weight')
elif result < 30:
    print('Overweight')
else:
    print('Obese')
