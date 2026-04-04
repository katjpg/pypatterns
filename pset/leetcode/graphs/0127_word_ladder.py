from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([beginWord])
        visited = {beginWord}
        steps = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        candidate = word[:i] + ch + word[i + 1 :]
                        if candidate in wordSet and candidate not in visited:
                            visited.add(candidate)
                            queue.append(candidate)
            steps += 1

        return 0


"""
time: O(m^2 * n) where m = word length, n = wordList size
- BFS visits at most n words.
- each word generates m * 26 candidates.
- building each candidate string is O(m).

space: O(m * n)
- wordSet and visited each hold up to n words of length m.

"""
