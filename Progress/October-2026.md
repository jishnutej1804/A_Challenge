# ⚡ October 2026

> **A_Challenge — Daily Progress**

---

## 📊 Progress

| 📅 Date | 📝 Work Completed | 🧠 Learning / Outcome | ✅ |
|:---:|:---|:---|:---:|
| Oct 01 | Solved Two Sum | HashMap • O(n) | ✅ |
| Oct 02 | Initialized EcoPulse sustainability tracker UI | Built responsive HTML/CSS/JS structure and tested desktop/mobile layout | ✅ |
| Oct 03 | Solved Valid Anagram | Frequency count array • O(n) • O(1) space | ✅ |
| Oct 04 | Created EcoPulse database schema and analytical queries | Practiced SELECT, SUM() and GROUP BY for carbon-emission analysis | ✅ |
| Oct 05 | Solved Valid Palindrome | Two Pointers • O(n) • O(1) space | ✅ |
| Oct 06 | Tested EcoPulse dynamic carbon calculator | Verified DOM-based calculation, reset functionality, and saved results persistence | ✅ |
| Oct 07 | Solved Two Sum II (Sorted Array) | Two Pointers • O(n) • O(1) space | ✅ |
| Oct 08 | Analyzed sample energy and waste emissions with Pandas | Calculated summary statistics and category-wise emission totals and averages | ✅ |
| Oct 09 | Solved Best Time to Buy and Sell Stock | Single Pass • O(n) time • O(1) space | ✅ |
| Oct 10 | Polished EcoPulse dashboard cards | Responsive UI • Hover effects • Reduced-motion support | ✅ |
| Oct 11 | Solved Valid Parentheses | Stack • LIFO • O(n) time | ✅ |
| Oct 12 | Implemented SQL JOINs and RANK | INNER/LEFT JOIN • Window Functions | ✅ |
| Oct 13 | Completed pre-travel codebase review | Reviewed documentation, EcoPulse files, SQL queries, Python EDA, and GitHub sync | ✅ |
| Oct 14 | Implemented Queue using Stacks | Created revision notes and tested a two-stack Python queue implementation | ✅ |
| Oct 15 | Solved Reverse Linked List | Three Pointers • O(n) time • O(1) space | ✅ |
| Oct 16 | Planned EcoPulse v2 system architecture and dashboard wireframe | System Design • Component Hierarchy • Data Flow | ✅ |
| Oct 17 | Implemented Binary Search and documented pseudocode and boundary conditions | DSA • Binary Search • O(log n) | ✅ |
| Oct 18 | Solved Search Insert Position & designed SQL queries | Binary Search Lower Bound • O(log n) • Window Functions | ✅ |
| Oct 19 | Solved Search in Rotated Sorted Array | Binary Search • Branch Selection • O(log n) | ✅ |
| Oct 20 | Documented ML Foundations: Decision Trees, Random Forests & Scaling | Gini Impurity • Entropy • Bagging • Feature Scaling | ✅ |
| Oct 21 | Binary Tree DFS Traversals & Maximum Depth | DFS (In/Pre/Postorder) • Recursion Stack • O(n) time • O(h) space | ✅ |
| Oct 22 | Invert / Flip Binary Tree | Tree Inversion • Recursion Base Case • O(n) time • O(h) space | ✅ |
| Oct 23 | Graph Representation & BFS Path Finding | Adjacency Matrix vs List • BFS Queue • Visited Set Cycle Prevention | ✅ |
| Oct 24 | Web Core Revision: Event Loop & REST | Microtasks vs Macrotasks • Promises Concurrency • HTTP Codes | ✅ |
| Oct 25 | Implemented Merge Intervals and documented the algorithm trace | Sorting • Interval Merging • O(n log n) | ✅ |
| Oct 26 | Solved Climbing Stairs using Dynamic Programming | Fibonacci Recurrence • O(n) Time • O(1) Space | ✅ |
| Oct 27 | — | — | ⬜ |
| Oct 28 | — | — | ⬜ |
| Oct 29 | — | — | ⬜ |
| Oct 30 | — | — | ⬜ |
| Oct 31 | — | — | ⬜ |

---

### 📈 Progress

**Completed:** 26 / 31

**Consistency:** █████████████████████████ 84%

---

> **No fixed schedule. No forced categories.**
>
> **Just show up and make progress.**

---

### 📌 Daily Deep Dives

#### Day 18: Search Insert Position
- **Category:** Binary Search / Lower Bound Pattern
- **Files Added:** `DSA/Arrays/day18_search_insert.py`, `DSA/Notes/DSA_Day18_Search_Insert_Position.md`
- **Key Takeaway:** Handled sorted array search and insertion bounds in $O(\log n)$ runtime and $O(1)$ space using safe midpoint calculations and left-pointer convergence when missing.

#### Day 19: Search in Rotated Sorted Array
- **Category:** Binary Search Application / Rotated Arrays
- **Files Added:** `DSA/Arrays/day19_search_rotated.py`, `DSA/Notes/DSA_Rotated_Binary_Search.md`
- **Key Takeaway:** Checking `nums[left] <= nums[mid]` deterministically identifies which half is strictly sorted, allowing standard range boundaries (`nums[left] <= target < nums[mid]`) to discard half the search space per iteration in $O(\log n)$ time.

#### Day 20: ML Foundations (Decision Trees, Random Forests & Scaling)
- **Category:** Machine Learning / Core Theory
- **Files Added:** `ML_Foundations_Summary.md`
- **Key Takeaway:** Tree-based models evaluate splits using Gini impurity or Information Gain and do not inherently require feature scaling. Random Forests combine bootstrap aggregation (bagging) with random feature subspace sampling to reduce variance and decorrelate individual trees.

#### Day 21: Binary Tree DFS & Maximum Depth
- **Category:** Trees / Depth-First Search (DFS) / Recursion
- **Files Added:** `DSA/Notes/DSA_Tree_DFS_Notes.md`
- **Key Takeaway:** Traversed binary trees using Inorder, Preorder, and Postorder recursive patterns. Solved Maximum Depth of Binary Tree using bottom-up postorder recursion with recurrence relation $\text{depth}(\text{node}) = 1 + \max(\text{depth}(\text{left}), \text{depth}(\text{right}))$ in $O(n)$ time and $O(h)$ auxiliary recursion call-stack space.


#### Day 22: Invert / Flip Binary Tree
- **Category:** Trees / Depth-First Search (DFS) / Recursion
- **Files Added:** `DSA/Notes/DSA_Invert_Tree_Pseudocode.md`
- **Key Takeaway:** Inverted a binary tree recursively by swapping left and right child pointers at each node. Identified the base case (`root is null`), traced recursive calls with an annotated tree diagram, and analyzed runtime ($O(n)$) and call-stack space ($O(h)$).

