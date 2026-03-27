class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        
        # condition 1 - if length of nums < 3, no triplet exists
        if n < 3:
            return []

        arr = sorted(nums)
        res = []

        for i in range(n - 2):
            
            # condition 2 - continue loop if start value has a duplicate 
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            # condition 3 - break loop if start value is positive
            if arr[i] > 0:
                break

            left = i + 1
            right = n - 1

            # condition 4 - converge left and right ptrs until left < right.
            while left < right:
                s = arr[i] + arr[left] + arr[right]

                # branch 4.1 - if sum is small, move left ptr to right by 1
                if s < 0:
                    left += 1

                # branch 4.2 - if sum is large, move right ptr to left by 1
                elif s > 0:
                    right -= 1

                # branch 4.3 - valid triplet found
                else:
                    
                    # add triplet to res[] list
                    res.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1

                    # condition 4.3.1 - skip duplicate left values
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1

                    # condition 4.3.2 - skip duplicate right values
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

        return res
    
    
"""
time: O(n^2)
- sorting takes O(n log n).
- the outer loop runs O(n) times.
- for each i, left and right scan array in O(n).
- O(n) * O(n) = O(n^2), which dominates O(n log n).

space: O(n)
- sorted(nums) creates a copy.
- pointers use O(1) extra space.

"""