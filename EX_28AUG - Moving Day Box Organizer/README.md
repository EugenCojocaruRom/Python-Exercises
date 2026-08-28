EX\_28AUG - Moving Day Box Organizer

Write a function organize\_moving\_boxes that takes boxes, weight\_limit and returns a dictionary of organized items by category.



The function processes moving boxes to organize items for the moving truck, skipping damaged boxes and stopping when the weight limit is reached.



Logic:



&#x20;   Skip boxes marked as "damaged" using continue

&#x20;   Stop processing when total weight exceeds the limit using break

&#x20;   Concatenate valid items into categories (furniture, electronics, clothes, books)

&#x20;   Track cumulative weight of processed boxes



Parameters:



&#x20;   boxes (list): List of dictionaries, each containing "items" (list), "weight" (int), "priority" (int), "status" (str)

&#x20;   weight\_limit (int): Maximum weight capacity for the moving truck



Returns: Dictionary with categories as keys and concatenated item lists as values. Format: {"furniture": \["sofa", "table"], "electronics": \["tv", "laptop"], "clothes": \["shirts", "pants"], "books": \["novel", "textbook"]}

