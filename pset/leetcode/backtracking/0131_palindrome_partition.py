class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def backtrack(start, curr):
            if start == len(s):
                res.append(curr[:])
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub == sub[::-1]:
                    curr.append(sub)
                    backtrack(end, curr)
                    curr.pop()

        backtrack(0, [])
        return res


"""
time: O(n * 2^n)
- 2^(n-1) ways to place partition cuts; palindrome check is O(n) per substring.

space: O(n)
- curr and recursion depth are at most n.

"""
