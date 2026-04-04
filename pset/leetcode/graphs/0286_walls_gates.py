from collections import deque

INF = 2147483647


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))


"""
time: O(m * n)
- each cell enqueued at most once.

space: O(m * n)
- queue holds at most all cells.

"""
