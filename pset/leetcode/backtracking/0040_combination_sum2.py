class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(start, curr, total):
            if total == target:
                res.append(curr[:])
                return
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return res


"""
time: O(2^n)
- include/exclude per element, sort + break prunes early.

space: O(n)
- curr and recursion depth are at most n.

"""
