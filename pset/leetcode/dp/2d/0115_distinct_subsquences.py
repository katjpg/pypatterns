class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        prev = [0] * (n + 1)
        prev[0] = 1

        for i in range(1, m + 1):
            cur = [0] * (n + 1)
            cur[0] = 1
            for j in range(1, n + 1):
                cur[j] = prev[j]
                if s[i - 1] == t[j - 1]:
                    cur[j] += prev[j - 1]
            prev = cur

        return prev[n]


"""
time: O(m * n)
- m = len(s), n = len(t).
- fill m rows of n entries.

space: O(n)
- two rows: prev and cur.

"""
