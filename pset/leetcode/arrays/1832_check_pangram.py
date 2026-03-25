class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashset = set()
        for ch in sentence:
            hashset.add(ch)
            if len(hashset) == 26:
                return True
        return False

""" 
time: O(n)
- iterate each n character in sentence.
- if length of sentence is n, iterate n times.

space: O(1)
- hashset stores characters in sentence
- max size is constant (O(26) == O(1)).

"""