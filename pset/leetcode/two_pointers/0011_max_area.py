class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            # compute area via current (width) * (shorter height)
            area = (right - left) * min(height[left], height[right])

            # keep largest area seen so far
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

"""
time: O(n)
- two pointers converge inward, each element visited once.
- pointer with shorter height moves inward each step.

space: O(1)
- only left, right, area, res.
- no extra data structures.

"""