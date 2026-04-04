class Solution:
    def numDecodings(self, s: str) -> int:
        a, b = 1, 0
        for i in range(len(s) - 1, -1, -1):
            cur = 0
            if s[i] != "0":
                cur = a
                if i + 1 < len(s) and int(s[i : i + 2]) <= 26:
                    cur += b
            a, b = cur, a
        return a


"""
time: O(n)
- single right -> left pass.

space: O(1)
- two variables: ways from i+1 and i+2.

"""
