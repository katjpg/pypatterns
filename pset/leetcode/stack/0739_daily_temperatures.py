class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res


"""
time: O(n)
- each idx pushed + popped from stack at most once.
- monotonic stack processes all elements in single pass.

space: O(n)
- res array of size n.
- stack holds at most n indices.

"""
