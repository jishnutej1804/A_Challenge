"""
Day 18: Search Insert Position (Binary Search Lower Bound)
"""

def search_insert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


if __name__ == "__main__":
    test_cases = [
        {"name": "Target in middle", "nums": [1, 3, 5, 6], "target": 5, "expected": 2},
        {"name": "Internal insertion point", "nums": [1, 3, 5, 6], "target": 2, "expected": 1},
        {"name": "Insert at tail", "nums": [1, 3, 5, 6], "target": 7, "expected": 4},
        {"name": "Insert at head", "nums": [1, 3, 5, 6], "target": 0, "expected": 0},
        {"name": "Empty list", "nums": [], "target": 10, "expected": 0},
        {"name": "Single item match", "nums": [5], "target": 5, "expected": 0},
        {"name": "Single item insert before", "nums": [5], "target": 2, "expected": 0},
        {"name": "Single item insert after", "nums": [5], "target": 8, "expected": 1},
    ]

    all_passed = True
    for tc in test_cases:
        actual = search_insert(tc["nums"], tc["target"])
        status = "PASS" if actual == tc["expected"] else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"[{status}] {tc['name']}: target={tc['target']} -> got {actual}, expected {tc['expected']}")

    print("\nResult:", "All tests passed!" if all_passed else "Some tests failed.")
