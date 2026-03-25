class Solution: 
    def containsDuplicate(self, nums: list[int]) -> bool: 
        hashset = set()
        for n in nums: 
            if n in hashset:
                return True
            hashset.add(n)
        return False

""" 
time: O(n)
- iterate through array once.
- set() lookup/add is O(1) on average.

space: O(n)
- hashset stores n elements.

"""
    

