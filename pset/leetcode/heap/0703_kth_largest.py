import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


"""
time: O(n log n) init, O(log k) per add
- heapify builds min-heap in O(n) -> pops n-k elements at O(log n) each.
- add pushes val and conditionally pops root (each sifts through at most log k levels).

space: O(k)
- self.heap stores only the k largest elements seen so far.
- popped elements below rank k are discarded.

"""
