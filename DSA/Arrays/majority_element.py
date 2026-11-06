def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# Test cases
print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
print(majority_element([5]))