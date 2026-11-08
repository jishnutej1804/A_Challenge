def valid_path(n, edges, source, destination):
    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        if node == destination:
            return True

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        return False

    return dfs(source)


print(valid_path(3, [[0, 1], [1, 2]], 0, 2))
print(valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
print(valid_path(3, [[0, 1], [1, 2]], 0, 0))