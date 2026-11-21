def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[left] <= nums[mid]:

            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Otherwise, the right half is sorted
        else:

            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
print(search([1], 0))
print(search([3, 1], 1))
print(search([5, 1, 3], 5))
print(search([], 0))