class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        window = {}
        res, resLen = [-1, -1], float('inf')
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            # char count in window meets target
            if c in countT and window[c] == countT[c]:
                have += 1

            # valid window, shrink from left to minimize
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left:right + 1] if resLen != float('inf') else ""

"""
time: O(m + n)
- build countT from t in O(n).
- each char in s visited at most twice (once by right, once by left).

space: O(m + n)
- countT holds at most n unique characters.
- window holds at most m unique characters.

"""