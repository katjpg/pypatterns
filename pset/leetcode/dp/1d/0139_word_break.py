class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        words = set(wordDict)

        for i in range(1, n + 1):
            for w in words:
                wl = len(w)
                if i >= wl and dp[i - wl] and s[i - wl : i] == w:
                    dp[i] = True
                    break

        return dp[n]


"""
time: O(n * m * k) where n = len(s), m = len(wordDict), k = max word length
- for each position, check each word.
- string comparison is O(k).

space: O(n)
- dp array of size n + 1.

"""
