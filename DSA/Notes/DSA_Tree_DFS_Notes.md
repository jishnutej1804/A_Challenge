\# Day 21 — Binary Tree DFS and Maximum Depth



\## 1. Binary Tree Basics



A binary tree is a hierarchical data structure where each node has at most two children:

\- Left child

\- Right child



Example tree used for all traces:



```text

&#x20;         1

&#x20;        / \\

&#x20;       2   3

&#x20;      / \\

&#x20;     4   5

```



\- Node `1` is the root.

\- Nodes `4`, `5`, and `3` are leaf nodes.



\---



\## 2. DFS Traversal Orders



Depth-First Search (DFS) traverses as deep as possible along each branch before backtracking.



\### A. Inorder Traversal: Left → Node → Right



\*\*Trace:\*\*

1\. Visit left subtree of `1` (goes to node `2`).

2\. Visit left subtree of `2`: output `4`.

3\. Output root of current subtree: `2`.

4\. Visit right subtree of `2`: output `5`.

5\. Return to root: output `1`.

6\. Visit right subtree of `1`: output `3`.



\*\*Output:\*\* `4 → 2 → 5 → 1 → 3`



```python

def inorder(node):

&#x20;   if node is None:

&#x20;       return

&#x20;   inorder(node.left)

&#x20;   print(node.val)

&#x20;   inorder(node.right)

```



\---



\### B. Preorder Traversal: Node → Left → Right



\*\*Trace:\*\*

1\. Output current node: `1`.

2\. Traverse left subtree: output `2`.

3\. Traverse left subtree of `2`: output `4`.

4\. Traverse right subtree of `2`: output `5`.

5\. Traverse right subtree of `1`: output `3`.



\*\*Output:\*\* `1 → 2 → 4 → 5 → 3`



```python

def preorder(node):

&#x20;   if node is None:

&#x20;       return

&#x20;   print(node.val)

&#x20;   preorder(node.left)

&#x20;   preorder(node.right)

```



\---



\### C. Postorder Traversal: Left → Right → Node



\*\*Trace:\*\*

1\. Visit left-most leaf: output `4`.

2\. Visit sibling leaf: output `5`.

3\. Output parent node: `2`.

4\. Visit right child of root: output `3`.

5\. Output root node: `1`.



\*\*Output:\*\* `4 → 5 → 2 → 3 → 1`



```python

def postorder(node):

&#x20;   if node is None:

&#x20;       return

&#x20;   postorder(node.left)

&#x20;   postorder(node.right)

&#x20;   print(node.val)

```



\---



\## 3. Maximum Depth of Binary Tree



\- \*\*Problem:\*\* Given the root of a binary tree, return its maximum depth.

\- \*\*Definition:\*\* The maximum depth is the number of nodes along the longest path from the root down to the farthest leaf node.



\### Recursive Formula



$$\\text{depth}(node) = 1 + \\max(\\text{depth}(node.left), \\text{depth}(node.right))$$



\### Base Case



$$\\text{depth}(\\text{None}) = 0$$



\### Python Implementation



```python

class TreeNode:

&#x20;   def \_\_init\_\_(self, val=0, left=None, right=None):

&#x20;       self.val = val

&#x20;       self.left = left

&#x20;       self.right = right



class Solution:

&#x20;   def maxDepth(self, root: TreeNode) -> int:

&#x20;       if root is None:

&#x20;           return 0



&#x20;       left\_depth = self.maxDepth(root.left)

&#x20;       right\_depth = self.maxDepth(root.right)



&#x20;       return 1 + max(left\_depth, right\_depth)

```



\### Depth Calculation on Example Tree:

\- $\\text{depth}(4) = 1 + \\max(0, 0) = 1$

\- $\\text{depth}(5) = 1 + \\max(0, 0) = 1$

\- $\\text{depth}(2) = 1 + \\max(1, 1) = 2$

\- $\\text{depth}(3) = 1 + \\max(0, 0) = 1$

\- $\\text{depth}(1) = 1 + \\max(2, 1) = 3$



\*\*Answer:\*\* `3`



\---



\## 4. Recursion Call Stack and Return Values



Execution flow for `maxDepth(root=1)`:



```text

maxDepth(1)

├── maxDepth(2)

│   ├── maxDepth(4)

│   │   ├── maxDepth(None) -> returns 0

│   │   └── maxDepth(None) -> returns 0

│   │   └── returns 1 + max(0, 0) = 1

│   ├── maxDepth(5)

│   │   ├── maxDepth(None) -> returns 0

│   │   └── maxDepth(None) -> returns 0

│   │   └── returns 1 + max(0, 0) = 1

│   └── returns 1 + max(1, 1) = 2

├── maxDepth(3)

│   ├── maxDepth(None) -> returns 0

│   └── maxDepth(None) -> returns 0

│   └── returns 1 + max(0, 0) = 1

└── returns 1 + max(2, 1) = 3

```



\---



\## 5. Complexity Analysis



\- Let $n$ be the number of nodes in the binary tree.

\- Let $h$ be the height of the tree.



| Metric | Complexity | Explanation |

| :--- | :--- | :--- |

| \*\*Time Complexity\*\* | $\\mathcal{O}(n)$ | Every node in the tree is visited exactly once. |

| \*\*Space Complexity (Balanced)\*\* | $\\mathcal{O}(\\log n)$ | Call stack depth corresponds to tree height $h \\approx \\log\_2(n)$. |

| \*\*Space Complexity (Worst / Skewed)\*\* | $\\mathcal{O}(n)$ | Call stack depth when every node has only one child. |



\---



\## 6. Common Pitfalls \& Mistakes



1\. \*\*Incorrect Base Case Return Value:\*\* Returning `1` instead of `0` when encountering a `None` node adds extra artificial depth.

2\. \*\*Taking Minimum Instead of Maximum:\*\* Using `min()` instead of `max()` calculates the shortest path or causes unintended zeros if unbalanced.

3\. \*\*Node Count vs. Edge Count:\*\* Some problem definitions ask for edge count ($edges = nodes - 1$); LeetCode 104 specifically counts nodes along the path.

4\. \*\*Traversal Mixing:\*\* Forgetting that the position of the node evaluation relative to recursive calls dictates whether it is Preorder, Inorder, or Postorder.



\---



\## 7. Key Takeaways



\- \*\*Inorder:\*\* Left $\\rightarrow$ Node $\\rightarrow$ Right (yields sorted sequence in a Binary Search Tree).

\- \*\*Preorder:\*\* Node $\\rightarrow$ Left $\\rightarrow$ Right (useful for cloning/serializing trees).

\- \*\*Postorder:\*\* Left $\\rightarrow$ Right $\\rightarrow$ Node (useful for bottom-up aggregations like depth, subtree sizes, and deletions).

\- Maximum depth is a direct postorder computation because children depths must resolve before calculating the parent's depth.

