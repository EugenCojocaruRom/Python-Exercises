EX\_17JUL - Ancient Plant Analysis

Create a function named analyze\_ancient\_plants that receives plant\_data and operation as its parameters.



The task is to analyze the historical uses of ancient plants in a sunlit laboratory garden. Each plant has a unique identifier and a list of integers representing its known uses over several centuries.



The function should perform different operations based on the input:



&#x20;   If the operation is "sum", calculate the total number of uses for each plant.

&#x20;   If the operation is "product", calculate the product of the uses for each plant.

&#x20;   If the operation is "reverse", reverse the list of uses for each plant.



Implement the following advanced techniques:



&#x20;   Use advanced arithmetic operations to handle large numbers efficiently.

&#x20;   Utilize break and continue statements to skip centuries with zero or negative values.

&#x20;   Apply an efficient reversing algorithm for the "reverse" operation.



Parameters:



&#x20;   plant\_data (dict): A dictionary where keys are plant identifiers (strings) and values are lists of integers representing the number of uses per century.

&#x20;   operation (str): A string specifying the operation to perform. It can be "sum", "product", or "reverse".



The function returns a dictionary where keys are plant identifiers and values depend on the operation performed:



&#x20;   For "sum": integer representing the total number of uses

&#x20;   For "product": integer representing the product of uses

&#x20;   For "reverse": list of integers with the order of uses reversed



