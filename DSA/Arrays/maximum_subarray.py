def maximum_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Test cases
print(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maximum_subarray([1]))
print(maximum_subarray([5, 4, -1, 7, 8]))
print(maximum_subarray([-2, -1, -3]))