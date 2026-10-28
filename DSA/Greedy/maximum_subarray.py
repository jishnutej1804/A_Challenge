def max_sub_array(nums):
    if not nums:
        raise ValueError("The input array must not be empty.")

    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-2, -3, -1, -5], -1),
        ([0, 0, 0], 0),
    ]

    for nums, expected in test_cases:
        result = max_sub_array(nums)
        print(f"Input: {nums}")
        print(f"Maximum subarray sum: {result}")
        print(f"Expected: {expected}")
        print(f"Passed: {result == expected}")
        print()