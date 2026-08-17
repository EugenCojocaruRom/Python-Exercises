# -------------------------------------------------------------------
# Part 1: Custom HashSet / HashMap Implementation
# -------------------------------------------------------------------
class CustomHashSet:
    def __init__(self, capacity=101):
        self.capacity = capacity
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        #Custom polynomial rolling hash function for string keys.
        hash_val = 0
        p = 31
        m = 10**9 + 7
        for char in key:
            hash_val = (hash_val * p + ord(char)) % m
        return hash_val % self.capacity

    def add(self, key):
        #Adds or updates key frequency count.
        index = self._hash(key)
        bucket = self.buckets[index]

        for entry in bucket:
            if entry[0] == key:
                entry[1] += 1
                return

        bucket.append([key, 1])

    def get_items(self):
        #Returns all (key, count) pairs.
        items = []
        for bucket in self.buckets:
            for key, count in bucket:
                items.append((key, count))
        return items

# -------------------------------------------------------------------
# Input Parsing
# -------------------------------------------------------------------
# Sample Input Data embedded directly to make the script self-contained
SAMPLE_INPUT = """4
IS01ABC
B100XYZ
IS01ABC
CJ99DEF
3 5
ALICE
XXXXX
XXXXE
2
ALICE
BOB
5
1 2 3 4 5
3 4 5 1 2
"""

# Split input by whitespace tokens to safely handle standard input or formatted strings
input_data = SAMPLE_INPUT.split()

if input_data:
    ptr = 0

    # 1. Read Vehicle Detections
    n = int(input_data[ptr])
    ptr += 1

    plates = []
    for _ in range(n):
        plates.append(input_data[ptr])
        ptr += 1

    # 2. Read Grid Dimensions & Grid
    rows = int(input_data[ptr])
    cols = int(input_data[ptr + 1])
    ptr += 2

    grid = []
    for _ in range(rows):
        grid.append(input_data[ptr])
        ptr += 1

    # 3. Read Volunteer Names
    num_names = int(input_data[ptr])
    ptr += 1

    volunteer_names = []
    for _ in range(num_names):
        volunteer_names.append(input_data[ptr])
        ptr += 1

    # 4. Read Checkpoint Fuel Data
    num_checkpoints = int(input_data[ptr])
    ptr += 1

    fuel_available = []
    for _ in range(num_checkpoints):
        fuel_available.append(int(input_data[ptr]))
        ptr += 1

    fuel_needed = []
    for _ in range(num_checkpoints):
        fuel_needed.append(int(input_data[ptr]))
        ptr += 1

    # -------------------------------------------------------------------
    # Task 1: Process Plates using Custom HashSet
    # -------------------------------------------------------------------
    plate_tracker = CustomHashSet()
    for plate in plates:
        plate_tracker.add(plate)

    # Get items and sort alphabetically by plate key
    unique_plates = sorted(plate_tracker.get_items(), key=lambda x: x[0])

    # -------------------------------------------------------------------
    # Task 2: Search Grid for Volunteer Names (8 Directions)
    # -------------------------------------------------------------------
    directions = [
        (0, 1),    # Right
        (0, -1),   # Left
        (1, 0),    # Down
        (-1, 0),   # Up
        (1, 1),    # Down-Right
        (1, -1),   # Down-Left
        (-1, 1),   # Up-Right
        (-1, -1)   # Up-Left
    ]

    def search_word(word):
        w_len = len(word)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == word[0]:
                    for dr, dc in directions:
                        match = True
                        for i in range(w_len):
                            nr, nc = r + dr * i, c + dc * i
                            if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == word[i]):
                                match = False
                                break
                        if match:
                            return True
        return False

    found_names = [name for name in volunteer_names if search_word(name)]

    # -------------------------------------------------------------------
    # Task 3: Find Starting Checkpoint Circuit
    # -------------------------------------------------------------------
    def find_start_checkpoint():
        for start in range(num_checkpoints):
            tank = 0
            possible = True
            for step in range(num_checkpoints):
                curr = (start + step) % num_checkpoints
                tank += fuel_available[curr]
                if tank < fuel_needed[curr]:
                    possible = False
                    break
                tank -= fuel_needed[curr]

            if possible:
                return start
        return -1

    start_index = find_start_checkpoint()

    # -------------------------------------------------------------------
    # Output Results
    # -------------------------------------------------------------------
    print("--- Task 1: Unique License Plate Counts ---")
    for plate, count in unique_plates:
        print(f"{plate}: {count}")

    print("\n--- Task 2: Found Volunteer Names ---")
    for name in found_names:
        print(name)

    print("\n--- Task 3: Valid Circuit Starting Checkpoint ---")
    print(start_index)