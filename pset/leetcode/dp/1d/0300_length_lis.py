class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        for val in nums:
            lo, hi = 0, len(tails)
            while lo < hi:
                mid = (lo + hi) // 2
                if tails[mid] < val:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == len(tails):
                tails.append(val)
            else:
                tails[lo] = val
        return len(tails)


"""
time: O(n log n)
- one pass over n elements.
- binary search on tails is O(log n) each.

space: O(n)
- tails array grows up to n in worst case (already sorted input).

"""
