class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // cols][mid % cols]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

"""
time: O(log(m * n))
- single binary search over 1D array (m * n elements).
- mid maps -> row mid // cols, col mid % cols.

space: O(1)
- only left, right, mid, val.
- no extra data structures.

"""
