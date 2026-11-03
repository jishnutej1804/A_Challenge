def move_zeroes(nums):
    position = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[position], nums[i] = nums[i], nums[position]
            position += 1

    return nums


# Test cases
print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes([0, 0, 1]))
print(move_zeroes([1, 2, 3]))
print(move_zeroes([0, 0, 0]))