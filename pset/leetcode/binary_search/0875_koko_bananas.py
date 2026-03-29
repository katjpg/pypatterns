class Solution:
    def canFinish(self, piles, h, k):
        total = 0
        for p in piles:
            total += (p + k - 1) // k
            if total > h:
                return False
        return True

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = (sum(piles) + h - 1) // h
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if self.canFinish(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return left

"""
time: O(n * log M) where n = len(piles), M = max(piles)
- binary search over k in [1, M]: log(M) iterations.
- each iteration scans all n piles in canFinish.
- note: log M depends on pile values, not array length.

space: O(1)
- only left, right, mid, total.
- no extra data structures.

"""