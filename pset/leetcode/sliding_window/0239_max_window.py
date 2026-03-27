class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = []
        res = []

        for i in range(len(nums)):
            # remove indices outside the window
            if dq and dq[0] <= i - k:
                dq.pop(0)

            # remove smaller values from back (can never be max)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # window is full, record the max (front of deque)
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res

"""
time: O(n)
- each index added and removed from deque at most once.
- monotonic deque keeps front as window maximum.

space: O(k)
- deque holds at most k indices.
- res holds n - k + 1 results.

"""