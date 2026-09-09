class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, reverse=True)
        m = -1
        ans = 0
        for pos, sp in cars:
            t = (target-pos) / sp
            if m == -1 or t > m:
                ans += 1
                m = t
        return ans
        