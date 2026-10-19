"""
Day 19: Search in Rotated Sorted Array (LeetCode #33)
"""

def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Check if the left half is normally sorted
        if nums[left] <= nums[mid]:
            # Target lies strictly inside the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, the right half is guaranteed sorted
        else:
            # Target lies strictly inside the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    test_cases = [
        {"name": "Target in right rotated segment", "nums": [4, 5, 6, 7, 0, 1, 2], "target": 0, "expected": 4},
        {"name": "Target missing in rotated array", "nums": [4, 5, 6, 7, 0, 1, 2], "target": 3, "expected": -1},
        {"name": "Target in left rotated segment", "nums": [4, 5, 6, 7, 0, 1, 2], "target": 5, "expected": 1},
        {"name": "Single element - match", "nums": [1], "target": 1, "expected": 0},
        {"name": "Single element - missing", "nums": [1], "target": 0, "expected": -1},
        {"name": "Two elements rotated - find first", "nums": [3, 1], "target": 3, "expected": 0},
        {"name": "Two elements rotated - find second", "nums": [3, 1], "target": 1, "expected": 1},
        {"name": "Unrotated array - normal search", "nums": [1, 2, 3, 4, 5, 6], "target": 4, "expected": 3},
    ]

    all_passed = True
    for tc in test_cases:
        actual = search(tc["nums"], tc["target"])
        status = "PASS" if actual == tc["expected"] else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"[{status}] {tc['name']}: target={tc['target']} -> got {actual}, expected {tc['expected']}")

    print("\nResult:", "All tests passed!" if all_passed else "Some tests failed.")
