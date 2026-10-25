\# Merge Intervals — Day 18



\## 1. Problem Definition

Given a list of intervals, merge all overlapping intervals and return a list of non-overlapping intervals.



\*\*Example Input:\*\*

```text

\[\[1, 3], \[2, 6], \[8, 10], \[15, 18]]

```



\*\*Expected Output:\*\*

```text

\[\[1, 6], \[8, 10], \[15, 18]]

```



\---



\## 2. Algorithm

1\. \*\*Sort\*\* all intervals by their starting values.

2\. \*\*Add\*\* the first interval to the result list.

3\. \*\*Iterate\*\* through every remaining interval:

&#x20;  - If its start is less than or equal to the end of the last result interval (`current.start <= previous.end`), merge them by updating the end time: $\\max(\\text{previous.end}, \\text{current.end})$.

&#x20;  - Otherwise, add the current interval as a new entry.

4\. \*\*Return\*\* the merged list.



\---



\## 3. Pseudocode

```text

MERGE\_INTERVALS(intervals):

&#x20;   if intervals is empty:

&#x20;       return \[]



&#x20;   sort intervals by start time

&#x20;   merged = \[first interval]



&#x20;   for each current interval from the second interval:

&#x20;       previous = last interval in merged



&#x20;       if current.start <= previous.end:

&#x20;           previous.end = max(previous.end, current.end)

&#x20;       else:

&#x20;           add current interval to merged



&#x20;   return merged

```



\---



\## 4. Trace Example



\*\*Input:\*\* `\[\[1, 3], \[2, 6], \[8, 10], \[15, 18]]`  

\*\*After sorting:\*\* `\[\[1, 3], \[2, 6], \[8, 10], \[15, 18]]`



| Current Interval | Comparison | Action | Merged State |

| :--- | :--- | :--- | :--- |

| Initial | — | Add first interval | `\[\[1, 3]]` |

| `\[2, 6]` | $2 \\le 3$ | Merge with `\[1, 3]` | `\[\[1, 6]]` |

| `\[8, 10]` | $8 > 6$ | Add as a new interval | `\[\[1, 6], \[8, 10]]` |

| `\[15, 18]` | $15 > 10$ | Add as a new interval | `\[\[1, 6], \[8, 10], \[15, 18]]` |



\*\*Final Result:\*\* `\[\[1, 6], \[8, 10], \[15, 18]]`



\---



\## 5. Boundary Conditions

\- \*\*Empty input:\*\* Returns an empty list `\[]`.

\- \*\*Single interval:\*\* Remains unchanged.

\- \*\*Identical intervals:\*\* Merge cleanly into a single interval.

\- \*\*Nested intervals:\*\* Keep the larger ending value ($\\max(end\_1, end\_2)$).

\- \*\*Touching endpoints:\*\* Intervals like `\[1, 4]` and `\[4, 6]` merge because $\\text{start} \\le \\text{end}$ holds true ($4 \\le 4$).

\- \*\*Disjoint intervals:\*\* Remain completely separate.



\---



\## 6. Complexity Analysis

\- \*\*Time Complexity:\*\* $\\mathcal{O}(n \\log n)$ due to the sorting step. The single linear scan takes $\\mathcal{O}(n)$.

\- \*\*Auxiliary Space:\*\* $\\mathcal{O}(n)$ in the worst case (when no intervals overlap) to store the merged result.



\---



> ### Key Takeaway

> Always sort by start time first. Compare each interval's start with the end of the last merged interval, extending the previous end when they overlap.

