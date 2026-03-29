class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights + [0]):
            start = i
            # pop taller bars, compute their max rectangle
            while stack and stack[-1][1] >= h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            stack.append((start, h))

        return maxArea


"""
time: O(n)
- each bar pushed + popped at most once.
- single pass with monotonic increasing stack.

space: O(n)
- stack holds (start, height) tuples, at most n entries.

"""
