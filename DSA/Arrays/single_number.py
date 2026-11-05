def single_number(nums):
    result = 0

    for num in nums:
        result ^= num

    return result


# Test cases
print(single_number([4, 1, 2, 1, 2]))
print(single_number([2, 2, 1]))
print(single_number([7]))