class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        freq = {}
        for r in range(rows):
            for c in range(cols):
                freq[board[r][c]] = freq.get(board[r][c], 0) + 1

        for ch in word:
            if freq.get(ch, 0) < word.count(ch):
                return False

        if freq.get(word[0], 0) > freq.get(word[-1], 0):
            word = word[::-1]

        def backtrack(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[idx]:
                return False

            ch = board[r][c]
            board[r][c] = "#"

            found = (
                backtrack(r + 1, c, idx + 1)
                or backtrack(r - 1, c, idx + 1)
                or backtrack(r, c + 1, idx + 1)
                or backtrack(r, c - 1, idx + 1)
            )

            board[r][c] = ch
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True

        return False


"""
time: O(m * n * 4^L) where L = len(word)
- each cell is a potential start; from each, up to 4 directions explored per character.

space: O(L)
- recursion depth is at most L.
- board is marked in-place (no visited set).

"""
