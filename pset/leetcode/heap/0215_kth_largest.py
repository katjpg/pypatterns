import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])

        return heap[0]


"""
time: O(n log k)
- heapify is O(k).
- each of remaining n-k elements costs O(log k) when it enters the heap.

space: O(k)
- heap holds exactly k elements.

"""
