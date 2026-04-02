class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(idx, curr):
            if idx == len(digits):
                res.append(curr)
                return
            for ch in mapping[digits[idx]]:
                backtrack(idx + 1, curr + ch)

        backtrack(0, "")
        return res


"""
time: O(4^n * n) where n = len(digits)
- at most 4 letters per digit, n digits deep. Each combination is length n.

space: O(n)
- recursion depth is n.

"""
