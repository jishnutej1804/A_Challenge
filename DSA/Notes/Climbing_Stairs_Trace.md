\# Climbing Stairs — Dynamic Programming



\## Problem

You are climbing a staircase with `n` steps. Each time, you can climb either 1 or 2 steps. Find the total number of distinct ways to reach the top.



\## Approach

Use an iterative Dynamic Programming approach based on the Fibonacci recurrence.



\- To reach step `n`, the last move must come from step `n - 1` or step `n - 2`.

\- Therefore, `ways(n) = ways(n - 1) + ways(n - 2)`.

\- Store only the previous two results to save memory.



\## Example Trace



| Step | Calculation | Number of ways |

|---|---|---:|

| 1 | Base case | 1 |

| 2 | Base case | 2 |

| 3 | 2 + 1 | 3 |

| 4 | 3 + 2 | 5 |

| 5 | 5 + 3 | 8 |

| 6 | 8 + 5 | 13 |



\## Complexity

\- \*\*Time:\*\* O(n) — each step is calculated once.

\- \*\*Space:\*\* O(1) — only two previous results are stored.



\## Test Results

All six test cases passed for inputs 1 through 6.



