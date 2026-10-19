# Day 18: Search Insert Position & Bisect Patterns

## 1. Problem Overview
Given a sorted array of distinct integers and a target value:
- Return the index if the target is found.
- If not, return the index where it would be if it were inserted in order.
- **Complexity:** $O(\log n)$ runtime, $O(1)$ auxiliary space.

---

## 2. Invariant & Boundary Analysis
1. **Search Window:** Indices span `0` to `n - 1`. Insertion points span `0` through `n`.
2. **Loop Condition (`left <= right`):** Contracts search space until `left > right`.
3. **Midpoint & Invariants:**
   - $\text{mid} = \text{left} + \lfloor (\text{right} - \text{left}) / 2 \rfloor$ (prevents integer overflow).
   - `nums[mid] == target` -> return `mid`.
   - `nums[mid] < target` -> search right half: `left = mid + 1`.
   - `nums[mid] > target` -> search left half: `right = mid - 1`.
4. **Termination:** When missing, `left` settles on the index of the first element strictly greater than `target` (the precise insertion index).

---

## 3. Pseudocode
```text
function search_insert(arr, target):
    left = 0
    right = length(arr) - 1

    while left <= right:
        mid = left + floor((right - left) / 2)
        if arr[mid] == target:
            return mid
        else if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

---

### Verify Creation
Once you press Enter and the prompt returns to `PS C:\Users\SR\A_Challenge>`, verify the file was created:

```powershell
Test-Path .\DSA\Notes\DSA_Day18_Search_Insert_Position.md
