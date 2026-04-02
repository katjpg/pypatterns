class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(curr, opened, closed):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            if opened < n:
                backtrack(curr + "(", opened + 1, closed)
            if closed < opened:
                backtrack(curr + ")", opened, closed + 1)

        backtrack("", 0, 0)
        return res


"""
time: O(4^n / sqrt(n))
- the nth Catalan number bounds the number of valid combinations.
- each combination is length 2n.

space: O(n)
- recursion depth is at most 2n.

"""
