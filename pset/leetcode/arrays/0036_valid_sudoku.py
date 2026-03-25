class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        boardSize = 9
        rows = [set() for _ in range(boardSize)]
        cols = [set() for _ in range(boardSize)]
        grids = [set() for _ in range(boardSize)]
        
        for row in range(boardSize):
            for col in range(boardSize):
                idx = board[row][col]
                
                if idx == ".":
                    continue
                
                grid_idx = (row // 3) * 3 + (col // 3)
                grid = grids[grid_idx]
                
                if idx in (rows[row] | cols[col] | grid):
                    return False
                
                rows[row].add(idx)
                cols[col].add(idx)
                grid.add(idx)
        
        return True
""" 
time: O(1)
- boardSize is 9 x 9; constant num of cells

space: O(1)
- row, cols, and grids are fixed-size.

         c0 c1 c2 | c3 c4 c5 | c6 c7 c8
       -----------+----------+-----------
r0       g0 g0 g0 | g1 g1 g1 | g2 g2 g2
r1       g0 g0 g0 | g1 g1 g1 | g2 g2 g2
r2       g0 g0 g0 | g1 g1 g1 | g2 g2 g2
       -----------+----------+-----------
r3       g3 g3 g3 | g4 g4 g4 | g5 g5 g5
r4       g3 g3 g3 | g4 g4 g4 | g5 g5 g5
r5       g3 g3 g3 | g4 g4 g4 | g5 g5 g5
       -----------+----------+-----------
r6       g6 g6 g6 | g7 g7 g7 | g8 g8 g8
r7       g6 g6 g6 | g7 g7 g7 | g8 g8 g8
r8       g6 g6 g6 | g7 g7 g7 | g8 g8 g8

"""
