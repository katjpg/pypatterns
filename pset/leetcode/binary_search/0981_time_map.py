class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        vals = self.store.get(key, [])
        left, right = 0, len(vals) - 1

        while left <= right:
            mid = (left + right) // 2
            if vals[mid][1] <= timestamp:
                res = vals[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res


"""
time:
- set: O(1) per call, append to list.
- get: O(log n) per call, binary search over timestamps for that key.
- timestamps are strictly increasing, so list is already sorted.

space: O(n)
- n total (value, timestamp) pairs stored across all keys.

"""
