class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            for i in range(idx, len(word)):
                ch = word[i]
                if ch == ".":
                    return any(dfs(i + 1, node[k]) for k in node if k != "#")
                if ch not in node:
                    return False
                node = node[ch]
            return "#" in node

        return dfs(0, self.root)


"""
time: O(26^d * m) per search where m = word length, d = number of dots
- addWord: O(m), traverses/creates m nodes.
- search: each dot branches into up to 26 children.
- constraint limits d to at most 2, so 26^2 = 676 -> O(m) per search.

space: O(T) where T = total characters across all inserted words
- shared prefixes share trie nodes, so T <= sum of all word lengths.

"""
