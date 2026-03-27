class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = {}
        c2 = {}
        for i in range(len(s1)):
            c1[s1[i]] = 1 + c1.get(s1[i], 0)
            c2[s2[i]] = 1 + c2.get(s2[i], 0)

        if c1 == c2:
            return True

        for right in range(len(s1), len(s2)):
            # add right char to window
            c2[s2[right]] = 1 + c2.get(s2[right], 0)

            # remove left char from window
            left = right - len(s1)
            c2[s2[left]] -= 1
            if c2[s2[left]] == 0:
                del c2[s2[left]]

            if c1 == c2:
                return True

        return False

"""
time: O(n)
- fixed-size window slides across s2, each char added/removed in O(1).
- dict comparison is O(26) at most, constant for lowercase letters.

space: O(1)
- c1, c2 hold at most 26 lowercase letters.
- only left, right.

"""