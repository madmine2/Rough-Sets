from itertools import product

def generate_combinations(list_of_lists):
    # Use itertools.product to generate all combinations
    all_combinations = list(product(*list_of_lists))
    
    # Convert each combination tuple to a list
    result = [list(combination) for combination in all_combinations]
    
    return result

# Example
sublists = [['a', 'b', 'c'], ['1', '2'], ['X', 'Y']]

combinations = generate_combinations(sublists)

# Display the result
for combination in combinations:
    print(combination)