\# Day 17 — Binary Search Notes



\## 1. Definition



Binary Search is an efficient searching algorithm used to find a target element in a \*\*sorted array\*\*. It repeatedly divides the search range into two halves.



\## 2. Pseudocode



```text

BINARY\_SEARCH(arr, target):

&#x20;   left = 0

&#x20;   right = length(arr) - 1



&#x20;   while left <= right:

&#x20;       mid = left + (right - left) // 2



&#x20;       if arr\[mid] == target:

&#x20;           return mid

&#x20;       else if arr\[mid] < target:

&#x20;           left = mid + 1

&#x20;       else:

&#x20;           right = mid - 1



&#x20;   return -1

```



\## 3. Boundary Conditions



\- \*\*Empty array:\*\* `right = -1`, so the loop does not execute. Return `-1`.

\- \*\*Single element:\*\* The algorithm checks the only element.

\- \*\*Target at the beginning:\*\* The search moves the right boundary left.

\- \*\*Target at the end:\*\* The search moves the left boundary right.

\- \*\*Target absent:\*\* The search ends when `left > right`.

\- \*\*Target smaller than all elements:\*\* The right boundary eventually becomes less than `left`.

\- \*\*Target larger than all elements:\*\* The left boundary eventually becomes greater than `right`.



\## 4. Why use `left <= right`?



The condition includes the case where `left == right`, meaning one candidate element remains. Using `left < right` could skip checking that final element.



When the target is absent, the search range eventually becomes empty, meaning `left > right`. The loop terminates.



\## 5. Safe Midpoint Calculation



Instead of:



```text

mid = (left + right) // 2

```



use:



```text

mid = left + (right - left) // 2

```



In languages with fixed-width integer types, `left + right` may overflow when both values are large. The alternative avoids that particular overflow when the bounds are valid and nonnegative.



\## 6. Time and Space Complexity



\- Best-case time: O(1)

\- Average/worst-case time: O(log n)

\- Auxiliary space for iterative Binary Search: O(1)



\## 7. Key Reminder



Binary Search requires sorted data. After checking the midpoint, update the boundary past the midpoint using `mid + 1` or `mid - 1` so that the search range shrinks and the loop can terminate.

