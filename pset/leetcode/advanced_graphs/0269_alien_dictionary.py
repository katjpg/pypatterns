from collections import deque


class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        graph = {ch: set() for word in words for ch in word}
        indegree = {ch: 0 for ch in graph}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1[: len(w2)] == w2:
                return ""
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        queue = deque(ch for ch in indegree if indegree[ch] == 0)
        order = []

        while queue:
            ch = queue.popleft()
            order.append(ch)
            for nei in graph[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return "".join(order) if len(order) == len(graph) else ""


"""
time: O(C) where C = total chars across all words
- comparing adjacent words + building graph is O(C).
- Kahn's BFS is O(V + E) (where V = unique chars, E = ordering edges).

space: O(V + E)
- graph + indegree for unique characters.

"""
