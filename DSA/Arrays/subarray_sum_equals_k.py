def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0

    prefix_count = {0: 1}

    for num in nums:
        prefix_sum += num

        required_sum = prefix_sum - k

        if required_sum in prefix_count:
            count += prefix_count[required_sum]

        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count


print(subarray_sum([1, 1, 1], 2))
print(subarray_sum([1, 2, 3], 3))
print(subarray_sum([1, -1, 0], 0))
print(subarray_sum([1, 2, 1, 2], 3))
print(subarray_sum([1, 2, 3], 7))