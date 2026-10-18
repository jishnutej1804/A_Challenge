
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Calculate midpoint safely
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Test cases
numbers = [1, 3, 5, 7, 9, 11, 13]

print("Array:", numbers)
print("Search for 7:", binary_search(numbers, 7))
print("Search for 1:", binary_search(numbers, 1))
print("Search for 13:", binary_search(numbers, 13))
print("Search for 6:", binary_search(numbers, 6))
print("Search in empty array:", binary_search([], 5))
