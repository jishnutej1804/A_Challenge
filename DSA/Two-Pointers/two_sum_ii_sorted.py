# Problem: Two Sum II - Input Array Is Sorted
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return []


# Test Cases
print(two_sum([2, 7, 11, 15], 9))    # [1, 2]
print(two_sum([2, 3, 4], 6))          # [1, 3]
print(two_sum([-1, 0], -1))           # [1, 2]