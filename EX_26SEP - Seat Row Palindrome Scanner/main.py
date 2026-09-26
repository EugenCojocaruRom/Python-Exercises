#Print header and separator
print("<-- Seat Row Palindrome Scanner -->")
print("-----------------------------------")

seat_codes = ["A3B2B1A", "X9Y8Z7", "M3O2M1", "R1A2C1E", "L1E2V1E1L"]

#Define function to extract the letters from the seat code
def extract_letters(seat_code):
    letters = [char for char in seat_code if char.isalpha()]
    return letters

#Define function to check if the code is a palindrome after extracting the letters
def is_balanced(seat_code):
    letters = extract_letters(seat_code)
    return letters == letters[::-1]

#Loop over the seat codes and print the results
for row_number, code in enumerate(seat_codes, start=1):
    result = "Balanced" if is_balanced(code) else "Not balanced"
    print(f"Row {row_number}: {code} -> {result}")

#Count the balanced rows
balanced_count = len([code for code in seat_codes if is_balanced(code)])
print(f"{balanced_count} out of {len(seat_codes)} rows are balanced.")