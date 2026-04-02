import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0


"""
time: O(n log n)
- heapify builds max-heap (via negation) in O(n).
- each smash pops two + pushes at most one, so at most n-1 rounds each O(log n).

space: O(n)
- heap stores up to n negated stone weights.
- only first, second.

"""
