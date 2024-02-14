def find_largest_element(arr):
    if not arr:
        return None  # Handle empty array case

    largest_element = max(arr)
    return largest_element

# Example usage:
n = 5
arr = [1, 2, 3, 4, 5]

largest_element = find_largest_element(arr)

print(f"The largest element in the array is: {largest_element}")
