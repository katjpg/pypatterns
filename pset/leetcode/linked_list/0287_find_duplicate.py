class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


"""
time: O(n)
- Floyd's cycle detection: slow (1 step) and fast (2 steps) intersect within the cycle.
- slow resets to 0, both advance 1 step to locate the cycle entry point.

space: O(1)
- only slow, fast.
- no extra data structures.

"""
