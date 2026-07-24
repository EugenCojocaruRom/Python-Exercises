def manage_stand(inventory, orders):
    #Create empty dictionary
    stock = {}

    #Parse initial inventory
    for item_str in inventory:
        name, count_str, preservative = item_str.split(":")
        stock[name] = {
            "count": int(count_str),
            "preservative": preservative.lower().strip()
        }

    #Process orders
    for order_str in orders:
        name, qty_str = order_str.split(":")
        qty = int(qty_str)

        if name in stock:
            stock[name]["count"] = max(0, stock[name]["count"] - qty)

    #Build summary dictionary (only including items with count > 0)
    summary = {
        "fresh": {},
        "artificial": {}
    }

    for name, info in stock.items():
        category = info["preservative"]
        count = info["count"]

        #Only add to summary if stock is remaining (> 0)
        if count > 0 and category in summary:
            summary[category][name] = count

    return summary

#Test case 1
inventory_1 = [
    "apples:50:fresh",
    "jam:20:artificial",
    "carrots:30:fresh",
    "pickles:15:artificial"
]
orders_1 = [
    "apples:10",
    "jam:5",
    "carrots:30",  #Sells out completely
    "pickles:2"
]
result_1 = manage_stand(inventory_1, orders_1)
print("=== Test Case 1 ===")
print(result_1)

#Test case 2
inventory_2 = [
    "strawberries:10:FRESH ",  #Capitalized and extra space
    "canned_corn:8:artificial"
]
orders_2 = [
    "strawberries:25",  #Over-ordering 10 -> hits 0
    "canned_corn:3",
    "dragonfruit:5"     #Item not in inventory -> ignored safely
]
result_2 = manage_stand(inventory_2, orders_2)
print("=== Test Case 2 ===")
print(result_2)

#Test case 3
inventory_3 = [
    "peaches:12:fresh",
    "dried_mango:20:organic"  #Not 'fresh' or 'artificial'
]
orders_3 = [
    "peaches:2"
]
result_3 = manage_stand(inventory_3, orders_3)
print("=== Test Case 3 ===")
print(result_3)
print()
#Running the tests
if __name__ == "__main__":
    tests = [
        ("Test 1: Standard Workflow", inventory_1, orders_1),
        ("Test 2: Over-ordering & Edge Formatting", inventory_2, orders_2),
        ("Test 3: Non-standard Preservatives", inventory_3, orders_3)
    ]
    for title, inv, ords in tests:
        print(f"--- {title} ---")
        print(manage_stand(inv, ords))
        print()