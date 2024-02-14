def find_min_max(arr):
    if not arr:
        return None, None 

    minimum = min(arr)
    maximum = max(arr)

    return minimum, maximum


array = [5, 2, 9, 1, 7, 3]
min_element, max_element = find_min_max(array)

print(f"Minimum element: {min_element}")
print(f"Maximum element: {max_element}")
