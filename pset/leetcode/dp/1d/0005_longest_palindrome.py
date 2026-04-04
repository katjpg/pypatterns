class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right

        start, end = 0, 0
        for i in range(len(s)):
            for lo, hi in (expand(i, i), expand(i, i + 1)):
                if hi - lo > end - start:
                    start, end = lo, hi

        return s[start:end]


"""
time: O(n^2)
- 2n-1 centers, each expands up to O(n).

space: O(1)
- only pointers and the result slice.

"""
