class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord("A")] += 1

        mx = max(freq)
        mxcnt = freq.count(mx)

        return max((mx - 1) * (n + 1) + mxcnt, len(tasks))


"""
time: O(m) where m = len(tasks)
- one pass to count frequencies, O(26) to find mx and mxcnt.

space: O(1)
- freq array is fixed at 26 entries regardless of input size.

"""
