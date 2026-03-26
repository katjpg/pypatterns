class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []


"""
time: O(n)
- each loop moves one pointer inward.
- left and right each move at most n times total.
- no nested loop.

space: O(1)
- only uses pointer variables and one sum variable.
- no extra data structure is used.

"""
