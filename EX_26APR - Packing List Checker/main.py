#Have list with necessary items
#e.g. ["passport", "charger", "sunscreen", "toothbrush", "headphones", "wallet", "keys"]
while True:
    must_pack = [item.strip() for item in input("Enter essential items (comma separated): ").split(",")]
    if must_pack != [""]:
        break
    print("Please enter at least one item!")
#Have list with items in the bag
while True:
    in_bag = [item.strip() for item in input("Enter items in your bag (comma separated): ").split(",")]
    if in_bag != [""]:
        break
    print("Please enter at least one item!")
#e.g.["sunscreen", "keys", "headphones", "toothbrush", "umbrella", "snacks"]
#Filter items - necessary but not in bag
forgot_items = [item for item in must_pack if item not in in_bag]
#Count items that are necessary and in the bag
packed_count = len(must_pack) - len(forgot_items)
#Print how many essential items you got out of the total
print(f"You packed {packed_count}/{len(must_pack)} essentials")
#Filter items - in the bag, but not needed
not_needed_items = [item for item in in_bag if item not in must_pack]
#Set condition for items that are not needed
if not_needed_items:
    #Print items
    print(f"You don't need these items: {not_needed_items}")
#Set condition for all necessary items packed
if not forgot_items:
    #Print message
    print("You're all set, enjoy your trip!")
#Set condition for forgotten items
else:
    #Print message
    print(f"You still need to pack: {forgot_items}")