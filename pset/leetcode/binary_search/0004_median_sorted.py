class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # binary search on shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partX = (left + right) // 2
            partY = (m + n + 1) // 2 - partX

            maxLeftX = nums1[partX - 1] if partX > 0 else float("-inf")
            minRightX = nums1[partX] if partX < m else float("inf")
            maxLeftY = nums2[partY - 1] if partY > 0 else float("-inf")
            minRightY = nums2[partY] if partY < n else float("inf")

            # valid partition: left halves <= right halves
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            elif maxLeftX > minRightY:
                right = partX - 1
            else:
                left = partX + 1

        return 0.0


"""
time: O(log(min(m, n)))
- binary search partitions shorter array, O(log(min(m, n))) iterations.
- each iteration does O(1) boundary comparisons.

space: O(1)
- only partX, partY, and 4 boundary values (maxLeftX, minRightX, etc.).
- no merging.
- no auxiliary arrays.

"""
