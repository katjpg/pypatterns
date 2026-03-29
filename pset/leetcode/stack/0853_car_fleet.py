class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleets = 0
        prev = 0

        for pos, spd in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / spd
            if time > prev:
                fleets += 1
                prev = time

        return fleets


"""
time: O(n log n)
- sorting cars by position.
- single pass through sorted pairs to count fleets.

space: O(n)
- sorted zip creates a list of n pairs.
- only fleets counter and prev variable otherwise.

"""
