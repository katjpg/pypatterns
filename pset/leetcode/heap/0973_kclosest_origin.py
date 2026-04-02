import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for x, y in points:
            dist = -(x * x + y * y)
            heapq.heappush(heap, (dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]


"""
time: O(n log k)
- iterates all n points, each push/pop is O(log k) on a heap max at size k.
- skips sqrt (squared distances keep relative ordering).

space: O(k)
- heap holds at most k entries (dist, x, y).
- output list reuses same k elements.

"""
