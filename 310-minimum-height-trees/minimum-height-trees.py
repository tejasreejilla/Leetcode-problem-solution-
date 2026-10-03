from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Start with all leaves
        queue = deque()

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        remaining = n

        while remaining > 2:
            # Remove one layer of leaves
            size = len(queue)
            remaining -= size

            for _ in range(size):
                leaf = queue.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)