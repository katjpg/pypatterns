class Solution:
    def reverseVowels(self, s: str) -> str:
        start, end = 0, len(s) - 1
        vowels = set("aeiouAEIOU")
        word = list(s)
        
        while start < end:
            while start < end and word[start] not in vowels:
                start += 1

            while start < end and word[end] not in vowels:
                end -= 1

            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
        
        return ''.join(word)
    
""" 
time: O(n)
- two-pointer traversal via scanning string from both ends.
- each character is checked a constant n number of times.
- vowel lookup in set is O(1).

space: O(n)
- convert the string -> list to allow swapping.
- list takes O(n) extra space.
- vowel set and pointers take O(1) space.

"""