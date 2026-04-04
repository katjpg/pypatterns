from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        order = []

        while queue:
            u = queue.popleft()
            order.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return order if len(order) == numCourses else []


"""
time: O(V + E)
- V = numCourses, E = len(prerequisites).
- each course and edge processed once.

space: O(V + E)
- graph adjacency list, indegree array, and order list.

"""
