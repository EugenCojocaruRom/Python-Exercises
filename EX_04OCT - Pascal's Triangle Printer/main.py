#Print header and separator
print("<-- Pascal's Triangle Printer -->")
print("---------------------------------")

#Loop for validating the number of rows
while True:
    try:
        #Prompt user to specify the number of rows
        num_rows = int(input("Enter the number of rows: "))
        #Check that the limit value is positive
        if num_rows <= 0:
            print("The number of rows must be bigger than 0. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")

#Create function to go over the rows
def next_row(row):

    return [a + b for a, b in zip([0] + row, row + [0])]

#Create a list to hold the values of the triangle and initialize it to 1
triangle = [[1]]
#Loop over the number of rows (the first row already exists, so add num_rows - 1 more rows)
for _ in range(num_rows - 1):
    triangle.append(next_row(triangle[-1]))

#The last row is the widest, so its length sets the width
last_row_text = " ".join(str(n) for n in triangle[-1])
width = len(last_row_text)
#Loop over the rows of the triangle
for row in triangle:
    row_text = " ".join(str(n) for n in row)
    print(row_text.center(width))

print()
#Loop over the rows of the triangle
for index, row in enumerate(triangle):
    if sum(row) > 10:
        #Print the sum of each row
        print(f"Row {index} sum: {sum(row)}")

#Declare variable for largest number and apply the max() function to the maximum value of each row
largest_number = max(max(row) for row in triangle)
print(f"Largest number in the triangle: {largest_number}")