\# Invert / Flip Binary Tree (LeetCode 226)



\## 1. Problem Overview

\- \*\*Problem:\*\* Invert / Flip a Binary Tree (create a mirror image of the tree).

\- \*\*Core Operation:\*\* Swap the `left` and `right` child pointers of every node in the tree recursively.

\- \*\*Base Case:\*\* If the current node is `null` (`None`), do nothing and return `null`.



\---



\## 2. Recursive Pseudocode \& Python Implementation



\### Pseudocode

```text

function invertTree(root):

&#x20;   # Base Case: empty tree or leaf child

&#x20;   if root is null:

&#x20;       return null



&#x20;   # Swap left and right children

&#x20;   temp = root.left

&#x20;   root.left = root.right

&#x20;   root.right = temp



&#x20;   # Recursively invert the left and right subtrees

&#x20;   invertTree(root.left)

&#x20;   invertTree(root.right)



&#x20;   # Return the root of the inverted tree

&#x20;   return root

```



\### Clean Python Implementation

```python

class TreeNode:

&#x20;   def \_\_init\_\_(self, val=0, left=None, right=None):

&#x20;       self.val = val

&#x20;       self.left = left

&#x20;       self.right = right



class Solution:

&#x20;   def invertTree(self, root: TreeNode | None) -> TreeNode | None:

&#x20;       if not root:

&#x20;           return None

&#x20;       

&#x20;       # Swap pointers

&#x20;       root.left, root.right = root.right, root.left

&#x20;       

&#x20;       # Recurse down both subtrees

&#x20;       self.invertTree(root.left)

&#x20;       self.invertTree(root.right)

&#x20;       

&#x20;       return root

```



\---



\## 3. Annotated Diagram \& Dry-Run Trace



\### Original Tree Structure

```text

&#x20;        4

&#x20;      /   \\

&#x20;     2     7

&#x20;    / \\   / \\

&#x20;   1   3 6   9

```



\### Dry-Run Steps (Pre-order Traversal Style)



```text

\[Step 1] Visit root Node 4:

&#x20;        - Swap children: Left becomes 7, Right becomes 2.

&#x20;        

&#x20;              4

&#x20;            /   \\

&#x20;           7     2

&#x20;          / \\   / \\

&#x20;         6   9 1   3



\[Step 2] Recurse on new Left Child -> Node 7:

&#x20;        - Swap children of 7: Left becomes 9, Right becomes 6.

&#x20;        

&#x20;              4

&#x20;            /   \\

&#x20;           7     2

&#x20;          / \\   / \\

&#x20;         9   6 1   3



\[Step 3] Recurse on Node 9:

&#x20;        - Both left and right are null.

&#x20;        - Swap null with null (leaves 9 unchanged).

&#x20;        - Calls invertTree(null) for both children:

&#x20;            \* invertTree(null) hits Base Case -> returns null immediately!



\[Step 4] Recurse on Node 6:

&#x20;        - Both left and right are null.

&#x20;        - Swap null with null.

&#x20;        - Base cases hit -> returns.



\[Step 5] Recurse on new Right Child of 4 -> Node 2:

&#x20;        - Swap children of 2: Left becomes 3, Right becomes 1.

&#x20;        

&#x20;              4

&#x20;            /   \\

&#x20;           7     2

&#x20;          / \\   / \\

&#x20;         9   6 3   1



\[Step 6] Recurse on Node 3 \& Node 1:

&#x20;        - Base cases hit on their null children.

&#x20;        - Returns back up the recursion call stack to root 4.

```



\### Final Inverted Tree (Mirror)

```text

&#x20;        4

&#x20;      /   \\

&#x20;     7     2

&#x20;    / \\   / \\

&#x20;   9   6 3   1

```



\---



\## 4. Complexity Analysis

\- \*\*Time Complexity:\*\* $O(n)$, where $n$ is the number of nodes in the binary tree. Every node is visited exactly once.

\- \*\*Space Complexity:\*\* $O(h)$, where $h$ is the height of the tree.

&#x20; - Balanced Tree: $O(\\log n)$ recursive call-stack space.

&#x20; - Skewed / Degenerate Tree: $O(n)$ worst-case call-stack space.

