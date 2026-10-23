
from collections import deque


def valid_path(n, edges, source, destination):
    """Return True if an undirected graph has a path between two vertices."""
    if source == destination:
        return True

    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = {source}
    queue = deque([source])

    while queue:
        node = queue.popleft()

        if node == destination:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


if __name__ == "__main__":
    examples = [
        (3, [[0, 1], [1, 2]], 0, 2, True),
        (6, [[0, 1], [0, 2], [3, 4], [4, 5]], 0, 5, False),
        (1, [], 0, 0, True),
        (4, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
        (4, [[0, 1]], 0, 3, False),
    ]

    for n, edges, source, destination, expected in examples:
        result = valid_path(n, edges, source, destination)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"{status}: source={source}, destination={destination}, "
            f"expected={expected}, got={result}"
        )
