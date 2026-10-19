# Day 19: Search in Rotated Sorted Array

## 1. Problem Overview
- **Problem:** LeetCode #33 — Search in Rotated Sorted Array
- **Platform:** LeetCode
- **Complexity:** $O(\log n)$ runtime, $O(1)$ auxiliary space
- **Core Challenge:** The original array of distinct values was sorted in ascending order and rotated at an unknown pivot index $k$. At any division point `mid`, at least one half of the range (`[left..mid]` or `[mid..right]`) remains strictly sorted.

---

## 2. Decision Tree: Branch Selection

```text
                           [ left <= right ]
                                   │
                           mid = left + (right - left) // 2
                                   │
                         nums[mid] == target?
                                ├── YES ──> Return mid
                                └── NO
                                   │
                         nums[left] <= nums[mid]?
                                ├── YES (Left Half is Sorted)
                                │       │
                                │   nums[left] <= target < nums[mid]?
                                │       ├── YES ──> right = mid - 1
                                │       └── NO  ──> left  = mid + 1
                                │
                                └── NO  (Right Half is Sorted)
                                        │
                                    nums[mid] < target <= nums[right]?
                                        ├── YES ──> left  = mid + 1
                                        └── NO  ──> right = mid - 1

                  (Loop terminates when left > right)
                                   │
                              Return -1
```

---

## 3. Invariants & Boundary Analysis

1. **Identifying Monotonic Halves:**
   - **`nums[left] <= nums[mid]`:** The left half contains no pivot wrap-around and is strictly monotonic.
   - **`nums[left] > nums[mid]`:** The pivot lies inside the left portion, which guarantees the right half `[mid..right]` is strictly monotonic.

2. **Discarding Windows:**
   - **Case A: Left half sorted:**
     - If `nums[left] <= target < nums[mid]`: Target falls inside the left sorted range $\rightarrow$ `right = mid - 1`.
     - Otherwise: Discard left half $\rightarrow$ `left = mid + 1`.
   - **Case B: Right half sorted:**
     - If `nums[mid] < target <= nums[right]`: Target falls inside the right sorted range $\rightarrow$ `left = mid + 1`.
     - Otherwise: Discard right half $\rightarrow$ `right = mid - 1`.

3. **Boundary Conditions:**
   - Single-element arrays (`left == right`) execute correctly because `nums[left] <= nums[mid]` evaluates to `True`.
   - Inclusive bounds (`<=`) on array ends protect targets positioned at index `0` or index `n - 1`.

---

## 4. Pseudocode

```text
function search(nums, target):
    left = 0
    right = length(nums) - 1

    while left <= right:
        mid = left + floor((right - left) / 2)

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```