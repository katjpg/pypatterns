class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        vis = [False] * n
        res = []

        def backtrack(curr):
            if len(curr) == n:
                res.append(curr[:])
                return
            for i in range(n):
                if vis[i]:
                    continue
                vis[i] = True
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
                vis[i] = False

        backtrack([])
        return res


"""
time: O(n * n!)
- n! permutations, each copied in O(n).
- vis[i] check is O(1) per candidate.

space: O(n)
- curr, vis, and recursion depth are each at most n.

"""
