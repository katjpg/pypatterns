class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(start, curr):
            res.append(curr[:])
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return res


"""
time: O(n * 2^n)
- 2^n subsets total, each copied to res in O(n).

space: O(n)
- curr holds at most n elements.
- recursion depth is at most n.

"""
