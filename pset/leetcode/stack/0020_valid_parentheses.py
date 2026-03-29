class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return not stack


"""
time: O(n)
- each char pushed/popped at most once.
- hashmap lookup is O(1) per char.

space: O(n)
- stack holds at most n/2 unmatched left brackets.
- pairs hashmap is constant size (3 entries).

"""
