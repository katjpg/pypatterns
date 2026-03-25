class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        products = [1] * n 
        
        L_mult = 1  # baseline multiplier = 1
        for i in range(n):
            products[i] = L_mult
            L_mult *= nums[i]
            
        R_mult = 1
        
        for i in range(n - 1, -1, -1):  # range(start, stop, step)
            products[i] *= R_mult
            R_mult *= nums[i]
        
        return products
    
""" 
time: O(n)
- iterate through array from left/right once.

space: O(1)
- N_mult and R_mult product variables used.

"""