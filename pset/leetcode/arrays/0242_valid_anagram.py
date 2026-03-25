class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        
        for i in range(len(s)):
            
            # s gives +1
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else: 
                hashmap[s[i]] = 1
            
            # t gives -1
            if t[i] in hashmap:
                hashmap[t[i]] -= 1
            else:
                hashmap[t[i]] = -1
                
        for val in hashmap.values():
            
            # all 0s == anagram
            # s = "anagram", t = "nagaram"
            # {'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 0}
            if val != 0:
                return False
        return True
    
""" 
time: O(n)
- iterate through strings + check hashmap once.
- hashmap update/check is O(1) on average.

space: O(n)
- hashmap stores char counts.
- for lowercase english letters: O(26) == O(1).
- if chars not limited to fixed set: O(n).

"""