
from collections import deque

def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1

    queue = deque()

    for course in range(num_courses):
        if indegree[course] == 0:
            queue.append(course)

    completed = 0

    while queue:
        current = queue.popleft()
        completed += 1

        for neighbor in graph[current]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return completed == num_courses

print(can_finish(2, [[1, 0]]))
print(can_finish(2, [[1, 0], [0, 1]]))
print(can_finish(4, [[1, 0], [2, 1], [3, 2]]))
print(can_finish(3, [[1, 0], [2, 1], [0, 2]]))