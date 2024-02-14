def find_missing_number(nums):
    n = len(nums) + 1  # n is the range of numbers [0, n]

    
    expected_sum = n * (n - 1) // 2

    actual_sum = sum(nums)

    # The missing number is the difference between the expected sum and the actual sum
    missing_number = expected_sum - actual_sum

    return missing_number

nums = [3, 0, 1]
missing_number = find_missing_number(nums)

print(f"The missing number is: {missing_number}")
