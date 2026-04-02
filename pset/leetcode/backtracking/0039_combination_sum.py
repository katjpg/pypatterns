class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start, curr, total):
            if total == target:
                res.append(curr[:])
                return
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    continue
                curr.append(candidates[i])
                backtrack(i, curr, total + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return res


"""
time: O(n^(t/m))
- n = len(candidates), t = target, m = min(candidates).
- branching factor is n, max depth is t/m (picking the smallest candidate repeatedly).

space: O(t/m)
- curr and recursion depth are at most t/m.

"""
