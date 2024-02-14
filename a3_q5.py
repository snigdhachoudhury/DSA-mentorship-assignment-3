def move_zeros_to_end(nums):
   
    non_zeros = [num for num in nums if num != 0]

   
    zeros_count = len(nums) - len(non_zeros)
    result = non_zeros + [0] * zeros_count

    return result


nums = [0, 1, 0, 3, 12]
result = move_zeros_to_end(nums)

print(result)
