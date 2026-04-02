class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = {}
        for word in words:
            node = root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["#"] = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return

            child = node[ch]

            if "#" in child:
                res.append(child["#"])
                del child["#"]

            board[r][c] = "*"

            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "*":
                    dfs(nr, nc, child)

            board[r][c] = ch

            if not child:
                del node[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res


"""
time: O(m * n * 4^L) where L = max word length
- DFS from each cell, 4 directions per step, trie prunes empty branches.

space: O(W * L) where W = number of words
- trie stores all words.
- recursion depth at most L.

"""
