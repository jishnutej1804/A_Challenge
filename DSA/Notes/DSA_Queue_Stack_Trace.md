\# Day 14 — Implement Queue using Stacks



\## Problem

Implement a FIFO queue using two stacks.



\*\*LeetCode:\*\* https://leetcode.com/problems/implement-queue-using-stacks/



\## Approach

\- `in\_stack`: stores newly added elements.

\- `out\_stack`: provides elements for `pop()` and `peek()`.

\- When `out\_stack` is empty, transfer all elements from `in\_stack` to `out\_stack`.

\- Each transfer reverses the order, preserving FIFO behavior.



\## Example Trace



| Operation | in\_stack (bottom → top) | out\_stack (bottom → top) | Result |

|---|---|---|---|

| push(5) | \[5] | \[] | — |

| push(8) | \[5, 8] | \[] | — |

| push(12) | \[5, 8, 12] | \[] | — |

| pop() | \[] | \[12, 8] | Returns 5 |

| peek() | \[] | \[12, 8] | Returns 8 |



\## Complexity

\- `push()`: O(1)

\- `pop()`: Amortized O(1)

\- `peek()`: Amortized O(1)

\- `empty()`: O(1)



\## Key Learning

A queue follows FIFO, while a stack follows LIFO. Two stacks can implement a queue by reversing the element order during transfer.



\## Day 14 Status

\- \[ ] Note created

\- \[ ] Trace reviewed

\- \[ ] Saved locally

\- \[ ] Commit and push (only if GitHub access is available)

