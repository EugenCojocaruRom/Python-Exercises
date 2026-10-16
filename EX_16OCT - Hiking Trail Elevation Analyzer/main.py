#Print header and separator
print("<-- Hiking Trail Elevation Analyzer -->")
print("---------------------------------------")

#Create function for retrieving the changes in elevation
def get_changes(elevations):
    changes = []
    for i in range(1, len(elevations)):
        changes.append(elevations[i] - elevations[i-1])
    return changes

#Create function for rating the overall trail difficulty
def rate_difficulty(total_climb):
    if total_climb < 200:
        return "Easy"
    elif total_climb <= 400:
        return "Moderate"
    else:
        return "Hard"

def analyze_trail(elevations):
    # 1. Get the changes (reuse your get_changes function)
    elev_diffs = get_changes(elevations)

    # 2. Calculate total climb and total descent
    total_climb = sum([x for x in elev_diffs if x > 0])
    total_descent = sum([abs(x) for x in elev_diffs if x < 0])

    # 3. Get the difficulty (reuse your rate_difficulty function)
    difficulty = rate_difficulty(total_climb)

    # 4. Return everything in a dictionary
    return {
        "climb": total_climb,
        "descent": total_descent,
        "difficulty": difficulty,
    }

#Have a list of various elevation values
elevations = [350, 420, 515, 490, 610, 680, 680.3, 332, 655, 720, 700, 700, 640, 580, 600]
print(f"Trail elevations: {', '.join(map(str, elevations))}")
#Declare variable to store the elevation differences
elev_diffs = get_changes(elevations)
#Calculate total climb and total descent
total_climb = sum([x for x in elev_diffs if x > 0])
total_descent = sum([abs(x) for x in elev_diffs if x < 0])
#Print the results
print(f"\nTotal climb: {total_climb:.1f} m")
print(f"Total descent: {total_descent:.1f} m")

#Find and print the highest point
top_height = max(elevations)
for number, value in enumerate(elevations, start = 1):
    if value == top_height:
        print(f"Highest point: {value:.1f} m at checkpoint {number}")

#Find and print the steepest climb
big_climb = max(elev_diffs)
for number, value in enumerate(elev_diffs, start = 1):
    if value == big_climb:
        print(f"Steepest climb: +{value:.1f} m between checkpoints {number} and {number + 1}")

#Print header
print("\n<== Trail Profile ==>")
#Print the trail profile
for number, value in enumerate(elev_diffs, start = 1):
    if value > 0:
        print(f" Segment {number}: ↑ {value:+.1f} m")
    elif value < 0:
        print(f" Segment {number}: ↓ {value:.1f} m")
    else:
        print(f" Segment {number}: → flat terrain")

#Call the difficulty function to print the trail difficulty level
difficulty = rate_difficulty(total_climb)
print(f"\nTrail difficulty: {difficulty}")

#Count how many segments were uphill, downhill, or flat
uphill = len([x for x in elev_diffs if x > 0])
downhill = len([x for x in elev_diffs if x < 0])
flat = len([x for x in elev_diffs if x == 0])
#Print the results
print(f"\nUphill segments: {uphill}")
print(f"Downhill segments: {downhill}")
print(f"Flat: {flat}")

#Have 2 trails with values
trail_a = [350, 420, 515, 490, 610, 680, 655, 720, 700, 640, 580, 600]
trail_b = [100, 150, 130, 200, 260, 240, 300]
result_a = analyze_trail(trail_b)
result_b = analyze_trail(trail_a)
result_a = analyze_trail(trail_a)
result_b = analyze_trail(trail_a)
result_b = analyze_trail(trail_b)
print(f"Trail A: climb {result_a['climb']:.1f} m, descent {result_a['descent']:.1f} m, difficulty {result_a['difficulty']}")
print(f"Trail B: climb {result_b['climb']:.1f} m, descent {result_b['descent']:.1f} m, difficulty {result_b['difficulty']}")
if result_a["climb"] > result_b["climb"]:
    print("Trail A has more climbing")
elif result_a["climb"] < result_b["climb"]:
    print("Trail B has more climbing")
else:
    print("Trail A and B are similar")