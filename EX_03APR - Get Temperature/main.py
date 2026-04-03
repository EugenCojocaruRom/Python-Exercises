#Get input from user - cast string to int
temp = int(input('Enter temperature: '))
#Set conditions for the messages to be displayed
if temp < 0:
    print("It's freezing!")
elif temp < 15:
    print("It's cold.")
elif temp < 25:
    print("It's nice outside.")
else:
    print("It's hot!")
