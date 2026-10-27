# Day 27 — Offline DSA Solutions

## 1. Reverse Linked List

**File:** `DSA/Linked-List/reverse_linked_list.py`

**Approach:** Iterative pointer reversal.

The algorithm uses three pointers:
- `prev`: the previous node.
- `curr`: the current node.
- `next_node`: saves the next node before reversing the link.

**Verified result:** `1 -> 2 -> 3 -> 4 -> 5` becomes `5 -> 4 -> 3 -> 2 -> 1`.

**Time Complexity:** O(n) — each node is visited once.
**Auxiliary Space:** O(1) — only a fixed number of pointers are used.

## 2. Valid Parentheses

**File:** `DSA/Stack/valid_parentheses.py`

**Approach:** Stack.

Opening brackets are pushed onto the stack. For every closing bracket, the algorithm checks whether the most recent opening bracket matches it. The string is valid if no mismatch occurs and the stack is empty at the end.

**Verified result:** All 8 test cases passed.

**Time Complexity:** O(n) — each character is processed at most once.
**Auxiliary Space:** O(n) — the stack can hold up to n opening brackets.

## 3. Binary Search

**File:** `DSA/Binary-Search/binary_search.py`

**Approach:** Iterative binary search on a sorted array.

The algorithm checks the middle element and eliminates half of the remaining search range after each comparison.

**Verified result:** All 5 test cases passed, including an empty array and an absent target.

**Time Complexity:** O(log n) — the search range is halved each iteration.
**Auxiliary Space:** O(1) — only a fixed number of variables are used.

## Verification Summary

| Algorithm | Tests | Status |
|---|---:|---|
| Reverse Linked List | Output checked | PASS |
| Valid Parentheses | 8 | PASS |
| Binary Search | 5 | PASS |

All three existing implementations were executed successfully. No duplicate solution files were created.
