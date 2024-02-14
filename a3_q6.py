def find_index_of_num(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1


arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
num_to_find = 4

result = find_index_of_num(arr, num_to_find)

if result != -1:
    print(f"{num_to_find} is present at index {result}.")
else:
    print(f"{num_to_find} is not present in the array.")
