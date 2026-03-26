class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


""" 
time: O(n)
- iterate through the string with two pointers.
- each loop moves left, right, or both.
- each character is processed at most once.

space: O(1)
- only uses left and right pointers.
- no extra data structure is created.

"""
