class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        
        for i in strs:  
            
            # i = "eat"
            # sorted("eat") -> ['a', 'e', 't']
            # tuple(['a', 'e', 't']) -> ('a', 'e', 't')
            
            key = tuple(sorted(i))  # "eat" -> ('a', 'e', 't')
            
            if key not in hashmap:
                hashmap[key] = []   # {('a', 'e', 't'): ['eat', 'tea', 'ate']}
            
            hashmap[key].append(i)
        
        return list(hashmap.values())
    
""" 
time: O(n * k log k)
- iterate through all words.
- for each word of length k, sort its letters (k log k).

space: O(n * k)
- hashmap stores all grouped words.
- keys/groups grow with total input size.  

"""