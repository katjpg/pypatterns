class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        units = 0

        while left < right:
            
            # left is bottleneck, right wall guaranteed taller
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                units += leftMax - height[left]

            # right is bottleneck, left wall guaranteed taller
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                units += rightMax - height[right]

        return units

"""
time: O(n)
- two pointers converge inward, each index visited once.
- leftMax and rightMax updated in constant time per step.

space: O(1)
- only left, right, leftMax, rightMax, units.
- no extra data structures.

"""