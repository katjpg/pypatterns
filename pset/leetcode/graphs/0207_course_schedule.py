from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        cnt = 0

        while queue:
            u = queue.popleft()
            cnt += 1
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return cnt == numCourses


"""
time: O(V + E)
- V = numCourses, E = len(prerequisites).
- each course and prerequisite edge processed once.

space: O(V + E)
- graph adjacency list and indegree array.

"""
