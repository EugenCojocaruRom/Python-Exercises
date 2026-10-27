#Print header
print("<== Lost & Found Desk ==>")

#Have initial list of items
items = [
    "umbrella:black:Iasi",
    "backpack:blue:Bucharest",
    "wallet:brown:Iasi",
    "scarf:red:Cluj",
    "phone:black:Iasi",
    "umbrella:green:Cluj",
    "keys:silver:Bucharest",
    "gloves:black:Cluj",
]

#Parse the list
parsed_list = [item.split(":") for item in items]
for i, (item_name, color, location) in enumerate(parsed_list, start=1):
    print(f"{i}. {item_name} ({color}) - found at {location}")

#Counting the items found in each location
counts = {}
for item_name, color, location in parsed_list:
    if location in counts:
        counts[location] += 1
    else:
        counts[location] = 1
#Print header
print("\nItems per station:")
for location, count in counts.items():
    print(f" {location}: {count}")

print()
#Filter the black items
black_items = [item_name for item_name, color, location in parsed_list if color == "black"]
if not black_items:
    print("There are no black items.")
elif len(black_items) == 1:
    print(f"Found 1 black item: {black_items[0]}.")
else:
    print(f"Found {len(black_items)} black items: {', '.join(black_items)}.")

print()
#Find the busiest station
busiest_station = max(counts, key=counts.get)
print(f"Busiest station: {busiest_station}")

print()
#Prompt user to enter the name of a station to check
station = input("Enter station name: ").strip().title()
found_here = [item_name for item_name, color, location in parsed_list if location == station]
if not found_here:
    print(f"No items found at {station}.")
elif len(found_here) == 1:
    print(f"Found 1 item at {station}: {found_here[0]}.")
else:
    print(f"Found {len(found_here)} items at {station}: {', '.join(found_here)}.")