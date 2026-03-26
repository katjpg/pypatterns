class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}

        for n in nums:
            # nums = [1,1,1,2,2,3], k = 2
            # after all n: {1: 3, 2: 2, 3: 1}
            hashmap[n] = 1 + hashmap.get(n, 0)

        arr = []
        # after loop: [[3, 1], [2, 2], [1, 3]]
        for n, freq in hashmap.items():
            arr.append([freq, n])

        arr.sort()
        # [[1, 3], [2, 2], [3, 1]]

        topK = []
        while len(topK) < k:
            item = arr.pop()  # [3, 1], then [2, 2]
            val = item[1]  # 1, then 2
            topK.append(val)  # [1], then [1, 2]

        return topK


""" 
time: O(n log n)
- count freq with a hashmap.
- sort [freq, val] pairs.

space: O(n)
- hashmap stores freq.
- arr stores the [freq, val] pairs.
- topK stores up to k elements.

"""
