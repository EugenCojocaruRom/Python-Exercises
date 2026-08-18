#Create function to processes office storage items
def clean_storage_room(items):
    result = {
        "keep": [],
        "throw": []
    }

    for entry in items:
        #Handle standalone "stop" or "skip" items
        if entry == "stop":
            break
        if entry == "skip":
            continue

        parts = entry.split(":", 1)
        item_name = parts[0]
        tag = parts[1] if len(parts) > 1 else None

        #Handle "stop" or "skip" when passed as tags or item names
        if tag == "stop" or item_name == "stop":
            break
        if tag == "skip" or item_name == "skip":
            continue

        #Categorize valid items
        if tag == "good":
            result["keep"].append(item_name[::-1])
        elif tag == "bad":
            result["throw"].append(item_name[::-1])

    return result

# Test 1: Stopping early with standalone "stop"
input_1 = ["pen:good", "stop", "pencil:bad", "eraser:good"]
print("Input 1:", input_1)
print("Output 1:", clean_storage_room(input_1))
print("-" * 50)

# Test 2: Mix of "skip", tagged "stop", and untagged items
input_2 = [
    "reporP:good",  # -> Keep: Proper
    "rekraM:bad",  # -> Throw: Marker
    "skip",  # -> Skipped
    "repap:skip",  # -> Skipped
    "rehcratS:good",  # -> Keep: Starcher
    "xam",  # -> Ignored (no tag)
    "ksed:bad",  # -> Throw: desk
    "dend:stop",  # -> Stops loop
    "rennaCS:good"  # -> Not reached
]
print("Input 2:", input_2)
print("Output 2:", clean_storage_room(input_2))