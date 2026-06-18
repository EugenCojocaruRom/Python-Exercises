EX\_18JUN\_Coddy - Bakery Sales Data Processor

Your bakery cafe has expanded to multiple locations and uses binary inventory codes to track different product types. You need to process sales data by converting binary codes to decimal values, combining sales from all locations, and analyzing the data until reaching your daily sales target.



Write a function process\_bakery\_sales that takes binary\_codes, location1\_sales, location2\_sales, and target\_threshold and returns a list of processed sales data.



Logic:



&#x20;   Convert each binary code string to its decimal equivalent

&#x20;   Concatenate the two sales arrays into one combined list

&#x20;   Process the combined sales data in order, keeping a running total

&#x20;   Use continue to skip any negative sales values (returns/refunds)

&#x20;   Use break to stop processing when cumulative sales exceed the target threshold

&#x20;   Return a list containing: \[converted\_decimal\_codes, processed\_sales\_values, final\_cumulative\_total]



Parameters:



&#x20;   binary\_codes (list): List of binary strings representing inventory codes

&#x20;   location1\_sales (list): Sales data from first location

&#x20;   location2\_sales (list): Sales data from second location

&#x20;   target\_threshold (int): Sales target to reach before stopping



Returns: List containing three elements: converted decimal codes, processed sales values, and final cumulative total.

Format: \[\[decimal\_codes], \[processed\_sales], cumulative\_total]

