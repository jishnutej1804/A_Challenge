\# Day 23 — Graph Representation, BFS and DFS



\- \*\*Date:\*\* 2026-10-23

\- \*\*Phase:\*\* 2 — Travel / Offline

\- \*\*Topic:\*\* Graph Representation and Traversal

\- \*\*LeetCode:\*\* \[1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)

\- \*\*Difficulty:\*\* Easy



\---



\## 1. What is a graph?



A graph is a data structure made of:

\- \*\*Vertices (nodes):\*\* The objects in the graph.

\- \*\*Edges:\*\* The connections between vertices.



For this challenge, assume the graph is \*\*undirected\*\*. If there is an edge between $u$ and $v$, we can travel from $u$ to $v$ and from $v$ to $u$.



\### Example Edges

```text

\[\[0, 1], \[0, 2], \[1, 3], \[2, 4]]

```



\### Diagram

```text

&#x20;      0

&#x20;     / \\

&#x20;    1   2

&#x20;    |   |

&#x20;    3   4

```



There is a path from $3$ to $4$: $3 \\rightarrow 1 \\rightarrow 0 \\rightarrow 2 \\rightarrow 4$.



\---



\## 2. Adjacency Matrix vs Adjacency List



\### Adjacency Matrix

An adjacency matrix is a two-dimensional $n \\times n$ table. The cell at row $u$, column $v$ indicates whether an edge connects $u$ and $v$.



For the example graph:



```text

&#x20;   0  1  2  3  4

0   0  1  1  0  0

1   1  0  0  1  0

2   1  0  0  0  1

3   0  1  0  0  0

4   0  0  1  0  0

```



\- A `1` means an edge exists; a `0` means no edge exists.

\- Because the graph is undirected, the matrix is symmetric across the main diagonal.



\---



\### Adjacency List

An adjacency list stores each vertex alongside a list of its immediate neighbors.



```text

0: \[1, 2]

1: \[0, 3]

2: \[0, 4]

3: \[1]

4: \[2]

```



\---



\### Space and Operation Comparison



| Property | Adjacency Matrix | Adjacency List |

| :--- | :--- | :--- |

| \*\*Space\*\* | $\\mathcal{O}(V^2)$ | $\\mathcal{O}(V + E)$ |

| \*\*Check if edge exists\*\* | $\\mathcal{O}(1)$ | $\\mathcal{O}(\\text{deg}(v))$, worst-case $\\mathcal{O}(V)$ |

| \*\*Iterate over neighbors\*\* | $\\mathcal{O}(V)$ | $\\mathcal{O}(\\text{deg}(v))$ |

| \*\*Best suited for\*\* | Dense graphs | Sparse graphs |

| \*\*Memory with isolated nodes\*\* | $\\mathcal{O}(V^2)$ | $\\mathcal{O}(V + E)$ |



> \*\*Notation:\*\* $V$ is the number of vertices and $E$ is the number of edges. For a simple undirected graph, the adjacency list stores each edge in both endpoints' neighbor lists.

>

> \*\*Key Idea:\*\* An adjacency list is generally the better choice for this LeetCode problem because it allows visiting only actual neighbors.



\---



\## 3. Breadth-First Search (BFS)



BFS explores a graph in layers, visiting nearby vertices before moving farther away.



\- \*\*Data structure:\*\* Queue (FIFO — First In, First Out).

\- Add the starting vertex to the queue.

\- Mark it visited when adding it.

\- Remove the front vertex and inspect its neighbors.

\- Add each unvisited neighbor and mark it visited.

\- Continue until the destination is found or the queue is empty.



\### BFS Queue Dry Run



Using the example graph:

```text

&#x20;      0

&#x20;     / \\

&#x20;    1   2

&#x20;    |   |

&#x20;    3   4

```



Start at `0`. Assume neighbors are processed in the order shown in the adjacency list.



| Step | Vertex Processed | Queue After Processing | Visited Set |

| :---: | :---: | :---: | :---: |

| \*\*Initial\*\* | — | `\[0]` | `{0}` |

| \*\*1\*\* | `0` | `\[1, 2]` | `{0, 1, 2}` |

| \*\*2\*\* | `1` | `\[2, 3]` | `{0, 1, 2, 3}` |

| \*\*3\*\* | `2` | `\[3, 4]` | `{0, 1, 2, 3, 4}` |

| \*\*4\*\* | `3` | `\[4]` | `{0, 1, 2, 3, 4}` |

| \*\*5\*\* | `4` | `\[]` | `{0, 1, 2, 3, 4}` |



\*\*BFS order:\*\* $0 \\rightarrow 1 \\rightarrow 2 \\rightarrow 3 \\rightarrow 4$.



If the destination is `4`, the search can return `True` as soon as `4` is discovered or processed.



\### Why is `visited` necessary?

Graphs can contain cycles. For example, $0 \\leftrightarrow 1 \\leftrightarrow 3 \\leftrightarrow 0$ can cause infinite loops if visits are not tracked.



> \*\*Crucial Rule:\*\* Mark a vertex visited when you \*\*enqueue\*\* it, not later when you dequeue it. This prevents the same vertex from being inserted multiple times by different neighbors.



\---



\## 4. Depth-First Search (DFS)



DFS explores one branch as far as possible before backtracking.



\- Recursive DFS uses the call stack.

\- Iterative DFS typically uses an explicit stack.

\- Both should use a `visited` set to avoid cycles.



\### Recursive DFS Pseudocode

```python

def dfs(node):

&#x20;   if node in visited:

&#x20;       return



&#x20;   visited.add(node)



&#x20;   for neighbor in graph\[node]:

&#x20;       dfs(neighbor)

```



Starting from `0`, a DFS order for the example graph could be:

$$0 \\rightarrow 1 \\rightarrow 3 \\rightarrow 2 \\rightarrow 4$$

\*(The exact order depends on the neighbor iteration sequence).\*



\---



\### BFS vs DFS Comparison



| Property | BFS | DFS |

| :--- | :--- | :--- |

| \*\*Main structure\*\* | Queue (`collections.deque`) | Stack or recursion call stack |

| \*\*Exploration style\*\* | Layer by layer | Deep branch first |

| \*\*Visited set\*\* | Yes, for cyclic graphs | Yes, for cyclic graphs |

| \*\*Shortest path (unweighted)\*\* | Yes | Not guaranteed |

| \*\*Time (Adjacency List)\*\* | $\\mathcal{O}(V + E)$ | $\\mathcal{O}(V + E)$ |

| \*\*Auxiliary Space\*\* | $\\mathcal{O}(V)$ | $\\mathcal{O}(V)$, including stack depth |



\---



\## 5. LeetCode 1971 — Find if Path Exists in Graph



\### Problem in Plain English

You receive:

\- `n`: Number of vertices labelled $0$ through $n - 1$.

\- `edges`: Pairs of connected vertices.

\- `source`: Starting vertex.

\- `destination`: Target vertex.



\*\*Goal:\*\* Return `True` if any path connects `source` to `destination`. Otherwise, return `False`.



\### Approach

1\. Build an adjacency list.

2\. Start BFS at `source`.

3\. Maintain a `visited` set.

4\. If `destination` is reached, return `True`.

5\. If the queue empties without reaching the destination, return `False`.



\### Python Solution (BFS)

```python

from collections import deque

from typing import List





class Solution:

&#x20;   def validPath(

&#x20;       self,

&#x20;       n: int,

&#x20;       edges: List\[List\[int]],

&#x20;       source: int,

&#x20;       destination: int,

&#x20;   ) -> bool:

&#x20;       if source == destination:

&#x20;           return True



&#x20;       # 1. Build adjacency list

&#x20;       graph = \[\[] for \_ in range(n)]

&#x20;       for u, v in edges:

&#x20;           graph\[u].append(v)

&#x20;           graph\[v].append(u)



&#x20;       # 2. Setup BFS structures

&#x20;       visited = {source}

&#x20;       queue = deque(\[source])



&#x20;       # 3. Traverse

&#x20;       while queue:

&#x20;           node = queue.popleft()



&#x20;           if node == destination:

&#x20;               return True



&#x20;           for neighbor in graph\[node]:

&#x20;               if neighbor not in visited:

&#x20;                   visited.add(neighbor)

&#x20;                   queue.append(neighbor)



&#x20;       return False

```



\### Complexity

\- \*\*Building the adjacency list:\*\* $\\mathcal{O}(V + E)$ time.

\- \*\*BFS traversal:\*\* $\\mathcal{O}(V + E)$ time.

\- \*\*Total Time Complexity:\*\* $\\mathcal{O}(V + E)$.

\- \*\*Space Complexity:\*\* $\\mathcal{O}(V + E)$ for the graph and $\\mathcal{O}(V)$ additional space for `visited` and `queue`.



\---



\## 6. Trace the Solution



\### Input

```python

n = 6

edges = \[\[0, 1], \[0, 2], \[3, 4], \[4, 5]]

source = 0

destination = 5

```



The graph has two disconnected components:

```text

0 —— 1

|

2



3 —— 4 —— 5

```



\### Step-by-Step Trace

BFS starts at `0`:



| Step | Processed Vertex | Queue | Visited Set |

| :---: | :---: | :---: | :---: |

| \*\*Initial\*\* | — | `\[0]` | `{0}` |

| \*\*1\*\* | `0` | `\[1, 2]` | `{0, 1, 2}` |

| \*\*2\*\* | `1` | `\[2]` | `{0, 1, 2}` |

| \*\*3\*\* | `2` | `\[]` | `{0, 1, 2}` |



The queue becomes empty without visiting `5`, so the function returns `False`.



\---



\## 7. Edge Cases to Remember



1\. \*\*`source == destination`:\*\* Return `True` immediately.

2\. \*\*No edges and `source != destination`:\*\* Return `False`.

3\. \*\*Direct edge exists:\*\* `source` and `destination` directly connected; returns `True`.

4\. \*\*Long chain:\*\* Verify memory limits for deep recursion or large queues.

5\. \*\*Cyclic graph:\*\* The `visited` set avoids infinite cycles.

6\. \*\*Disconnected graph:\*\* The search only explores the connected component containing `source`.

7\. \*\*Multiple shared neighbors:\*\* Enqueue-time marking skips redundant additions.



\---



\## 8. Practice Tasks



\- \[ ] Draw the adjacency matrix and adjacency list for the example graph.

\- \[ ] Trace the BFS queue by hand on paper.

\- \[ ] Trace DFS using a stack or recursion.

\- \[ ] Explain why the visited set is updated when a vertex is enqueued.

\- \[ ] Implement the BFS solution without copying.

\- \[ ] Explain the time and space complexity in your own words.

\- \[ ] Solve the LeetCode problem and record the outcome.



\---



\## 9. Final Takeaway



An adjacency list represents connections efficiently for sparse graphs ($\\mathcal{O}(V + E)$ space). BFS uses a queue to explore layer by layer, while DFS uses a stack or recursion to explore deeper paths first. A `visited` set prevents repeated exploration in cyclic graphs. For checking reachability in an unweighted graph, either BFS or DFS works; BFS also guarantees the shortest path by edge count.

