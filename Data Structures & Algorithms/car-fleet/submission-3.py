class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, reverse=True)
        s = []
        for pos, sp in cars:
            t = (target-pos) / sp
            if not s or t > s[-1]:
                s.append(t)
        return len(s)
        