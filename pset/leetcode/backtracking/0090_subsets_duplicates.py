class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        def backtrack(start, curr):
            res.append(curr[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return res


"""
time: O(n * 2^n)
- up to 2^n subsets, each copied in O(n).
- duplicate skip reduces actual count but worst case is all unique.

space: O(n)
- curr and recursion depth are at most n.

"""
