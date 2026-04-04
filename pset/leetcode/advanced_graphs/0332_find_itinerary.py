class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = {}
        for src, dst in sorted(tickets, reverse=True):
            if src not in graph:
                graph[src] = []
            graph[src].append(dst)

        route = []

        def dfs(airport):
            while graph.get(airport):
                dfs(graph[airport].pop())
            route.append(airport)

        dfs("JFK")
        return route[::-1]


"""
time: O(E log E)
- sorting tickets dominates.
- each edge (ticket) visited exactly once during DFS.

space: O(V + E)
- adjacency list and route list.

"""
