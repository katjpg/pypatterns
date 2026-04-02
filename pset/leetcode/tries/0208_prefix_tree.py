class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True


"""
time: O(m) for insert, search, startsWith where m = length of word/prefix
- each operation traverses / creates at most m nested dicts.

space: O(T) where T = total characters across all inserted words
- each unique character in a prefix path creates one nested dict.
- shared prefixes reuse the same dict nodes, so T <= sum of all word lengths.

"""
