def process_bakery_sales(binary_codes, location1_sales, location2_sales, target_threshold):
    #Convert each binary code string to its decimal equivalent
    decimal_codes = [int(code, 2) for code in binary_codes]

    #Concatenate the two sales arrays into one combined list
    combined_sales = location1_sales + location2_sales
    processed_sales_values = []
    final_cumulative_total = 0

    #Process the combined sales data in order, keeping a running total
    for sale in combined_sales:
        #Use continue to skip any negative sales values (returns/refunds)
        if sale < 0:
            continue

        final_cumulative_total += sale
        processed_sales_values.append(sale)

        #Use break to stop processing when cumulative sales exceed the target threshold
        if final_cumulative_total > target_threshold:
            break

    #Return the required format: [[decimal_codes], [processed_sales], cumulative_total]
    return [decimal_codes, processed_sales_values, final_cumulative_total]

#Provide the binary codes as strings in a list
inventory_binary = ["101", "1010", "1100", "1111"]  # Decimals: 5, 10, 12, 15

#Provide the sales data for both locations (including some refunds/negative values)
loc1_data = [120, -50, 300, 150]
loc2_data = [450, -20, 200, 600]

#Define the daily sales target threshold
target = 800

#Call the function with these values and store the result
result = process_bakery_sales(inventory_binary, loc1_data, loc2_data, target)

#Print the output
print(result)