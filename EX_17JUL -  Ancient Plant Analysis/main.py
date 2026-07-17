def analyze_ancient_plants(plant_data, operation):
    result = {}
    for plant_id, uses in plant_data.items():
        if operation == "sum":
            total_sum = 0
            for count in uses:
                #Skip zero or negative values
                if count <= 0:
                    continue
                total_sum += count
            result[plant_id] = total_sum
        elif operation == "product":
            total_product = 1
            for count in uses:
                #Skip zero or negative values
                if count <= 0:
                    continue
                total_product *= count
            #If all values are skipped, it returns the identity element (1)
            result[plant_id] = total_product
        elif operation == "reverse":
            reversed_uses = list(uses)
            left, right = 0, len(reversed_uses) - 1
            while left < right:
                reversed_uses[left], reversed_uses[right] = reversed_uses[right], reversed_uses[left]
                left += 1
                right -= 1
            result[plant_id] = reversed_uses
    return result

#Setup the input data (th arguments)
plant_data_input = {
    "Mint": [1, 2, 3],
    "Lavender": [0, 0, 0]
}
operation_input = "product"

#Call the function and print the output
output = analyze_ancient_plants(plant_data_input, operation_input)
print(output)