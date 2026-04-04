class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        dist = [float("inf")] * n
        dist[src] = 0

        for _ in range(k + 1):
            prev = dist[:]
            for u, v, w in flights:
                if prev[u] != float("inf") and prev[u] + w < dist[v]:
                    dist[v] = prev[u] + w

        return dist[dst] if dist[dst] != float("inf") else -1


"""
time: O(k * E)
- k + 1 rounds, each checks all E edges for shorter paths.

space: O(n)
- dist array and its copy.

"""
