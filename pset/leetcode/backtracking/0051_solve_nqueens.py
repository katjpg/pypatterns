class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = []

        def backtrack(row):
            if row == n:
                sol = []
                for col in board:
                    r = ["."] * n
                    r[col] = "Q"
                    sol.append("".join(r))
                res.append(sol)
                return
            for col in range(n):
                if col in cols or (row + col) in posDiag or (row - col) in negDiag:
                    continue
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board.append(col)

                backtrack(row + 1)

                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                board.pop()

        backtrack(0)
        return res


"""
time: O(n!)
- row 0 has n choices, row 1 has at most n-1, etc
- set lookups prune in O(1).

space: O(n)
- board stores one column index per row. 
- cols, posDiag, negDiag each hold at most n entries.

"""
