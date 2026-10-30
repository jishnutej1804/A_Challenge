# Day 30 – Validate Binary Search Tree

## Problem
Validate whether a binary tree is a valid Binary Search Tree (BST).

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Topic:** Trees / Binary Search Tree

## Key Concept

A Binary Search Tree follows these rules:

1. All values in the left subtree must be smaller than the current node.
2. All values in the right subtree must be greater than the current node.
3. Duplicate values are not allowed.

## Approach: Recursive DFS with Bounds

Instead of comparing a node only with its parent, maintain a valid minimum and maximum range for every node.

- Left subtree: `(min_val, node.val)`
- Right subtree: `(node.val, max_val)`

Initially, the allowed range is `(-∞, +∞)`.

## Algorithm

1. Start with the root and an unlimited range.
2. If the current node is `None`, return `True`.
3. Check whether the node value is strictly within the allowed range.
4. If it is outside the range, return `False`.
5. Recursively validate the left and right subtrees with updated bounds.

## Python Implementation

```python
class Solution:
    def isValidBST(self, root):
        def validate(node, min_val, max_val):
            if node is None:
                return True

            if not (min_val < node.val < max_val):
                return False

            return (
                validate(node.left, min_val, node.val)
                and
                validate(node.right, node.val, max_val)
            )

        return validate(root, float('-inf'), float('inf'))
```

## Test Cases

| Input | Expected Output |
|---|---|
| `[2,1,3]` | `True` |
| `[5,1,4,null,null,3,6]` | `False` |

## Complexity Analysis

- **Time Complexity:** `O(n)` – Every node is visited once.
- **Space Complexity:** `O(h)` – Recursive call stack, where `h` is the tree height.

## Key Takeaway

The important concept is **boundary propagation**. Every node must satisfy the constraints inherited from all its ancestors, not just its immediate parent.

## Files

- `DSA/Trees/validate_bst.py`
- `DSA/Notes/DSA_Day30_Validate_BST.md`

## Commit Message

`Solve Validate Binary Search Tree using bounded recursive DFS`