def remove_duplicates(sequence):
    unique_elements = []
    seen = set()

    for item in sequence:
        if item not in seen:
            seen.add(item)
            unique_elements.append(item)

    if isinstance(sequence, tuple):
        return tuple(unique_elements)
    else:
        return unique_elements

# Sample input
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
