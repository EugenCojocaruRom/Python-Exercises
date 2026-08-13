#Print header and separator
print("<-- Health Data Analysis -->")
print("----------------------------")

import math

#Define function for converting an integer to a string
def convert_to_base(val, base_name):
    #Converting an integer to a string in the specified base
    val = int(val)
    if base_name == 'binary':
        return bin(val)[2:]
    elif base_name == 'hexadecimal':
        return hex(val)[2:].upper()
    elif base_name == 'octal':
        return oct(val)[2:]
    elif base_name == 'decimal':
        return str(val)
    else:
        raise ValueError(f"Unsupported base: {base_name}")

#Define function for analyzing the health data
def analyze_health_data(data, bases, operations):
    #Create empty list to store the decimal values
    decimal_values = []
    for item in data:
        val = item['value']
        base = item['base']
        if isinstance(val, str):
            dec_val = int(val, base)
        else:
            dec_val = int(str(val), base)
        decimal_values.append(dec_val)

    #Create empty dictionary to store the results of the conversions
    result = {}

    #Convert decimal values into requested base formats
    for base in bases:
        result[base] = [convert_to_base(val, base) for val in decimal_values]

    #Perform specified mathematical operations
    for op in operations:
        if op == 'average':
            result['average'] = sum(decimal_values) / len(decimal_values) if decimal_values else 0.0
        elif op == 'sum':
            result['sum'] = sum(decimal_values)
        elif op == 'product':
            result['product'] = math.prod(decimal_values)

    #Statistical metrics
    result['decimal_values'] = decimal_values

    if decimal_values:
        min_val = min(decimal_values)
        max_val = max(decimal_values)
        result['min'] = min_val
        result['max'] = max_val
        result['range'] = max_val - min_val
    else:
        result['min'] = None
        result['max'] = None
        result['range'] = 0

    return result

#Analyzing the data
data = [
    {'value': '1', 'base': 10},
    {'value': '1', 'base': 2},
    {'value': '1', 'base': 16}
]
bases = ['binary', 'hexadecimal', 'octal', 'decimal']
operations = ['average', 'sum', 'product']
output = analyze_health_data(data, bases, operations)
print(output)