# Read the number of booths
n = int(input("Enter the number of booths: "))

total_power = 0
vowels_set = "aeiouAEIOU"

for i in range(n):
    # Read booth name and power usage from SEPARATE lines
    booth_name = input("Enter booth name: ").strip()
    power = int(input("Enter power value: ").strip())

    # Extract all vowels present in this booth's name
    booth_vowels = [char for char in booth_name if char in vowels_set]

    # Reconstruct the name, popping from the end of our vowel list
    modified_name_list = []
    for char in booth_name:
        if char in vowels_set:
            modified_name_list.append(booth_vowels.pop())
        else:
            modified_name_list.append(char)

    modified_name = "".join(modified_name_list)

    # Add to total power
    total_power += power

    # Print the modified booth name
    print(f"Booth name: {modified_name}")

# Calculate and print energy rating based on total_power
if total_power <= 500:
    energy_rating = "A"
elif total_power <= 1000:
    energy_rating = "B"
elif total_power <= 1500:
    energy_rating = "C"
else:
    energy_rating = "D"

print(f"Energy rating: {energy_rating}")
