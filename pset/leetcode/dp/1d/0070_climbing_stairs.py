class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


"""
time: O(n)
- single pass from step 2 -> step n.

space: O(1)
- two variables track previous two values.

"""
