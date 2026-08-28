def organize_moving_boxes(boxes, weight_limit):
    organized_items = {
        "furniture": [],
        "electronics": [],
        "clothes": [],
        "books": []
    }

    current_weight = 0

    for box in boxes:
        #Skip damaged boxes
        if box.get("status") == "damaged":
            continue

        box_weight = box.get("weight", 0)

        #Stop processing if adding box exceeds limit
        if current_weight + box_weight > weight_limit:
            break

        #Add box weight
        current_weight += box_weight

        #Extract items and assign to category
        box_category = box.get("category")
        items = box.get("items", [])

        if box_category in organized_items:
            for item in items:
                #Support both simple strings ("chair") and dicts ({"name": "chair"})
                item_name = item.get("name") if isinstance(item, dict) else item
                if item_name:
                    organized_items[box_category].append(item_name)

    return organized_items


#Test run
if __name__ == "__main__":
    sample_boxes = [
        {
            "category": "furniture",
            "items": ["chair", "table"],
            "weight": 30,
            "status": "ok"
        },
        {
            "category": "electronics",
            "items": ["tv"],
            "weight": 20,
            "status": "damaged"  # Skipped
        },
        {
            "category": "books",
            "items": ["novel"],
            "weight": 80,  # 30 + 80 = 110 (exceeds limit of 100) -> triggers break
            "status": "ok"
        }
    ]

    result = organize_moving_boxes(sample_boxes, 100)
    print("Result:")
    print(result)