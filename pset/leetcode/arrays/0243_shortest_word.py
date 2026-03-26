class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        min_dist = len(wordsDict)
        i1, i2 = -1, -1
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                i1 = i
            elif wordsDict[i] == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                min_dist = min(min_dist, abs(i1 - i2))
        return min_dist


""" 
time: O(n)
- single pass through wordsDict.
- each word is checked once.
- all operations inside the loop are O(1).

space: O(1)
- only stores the last seen indices and current minimum distance.
- no extra data structure is used.

"""
