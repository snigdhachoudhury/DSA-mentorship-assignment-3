def is_sorted_and_rotated(arr):
    n = len(arr)
    rotations = 0

    # Find the number of rotations
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            rotations += 1

    # If there are no rotations or only one rotation, the array is sorted and rotated
    return rotations <= 1

# Example usage:
arr1 = [3, 4, 5, 1, 2]
arr2 = [1, 2, 3, 4, 5]
arr3 = [2, 3, 4, 5, 1]

print(is_sorted_and_rotated(arr1))  # True
print(is_sorted_and_rotated(arr2))  # True
print(is_sorted_and_rotated(arr3))  # True
