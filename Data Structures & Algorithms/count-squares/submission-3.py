class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for p, c in self.points.items():
            x1, y1 = p
            if x1 == x and y1 == y:
                continue
            if abs(x1 - x) == abs(y1 - y):
                p1, p2 = (x1, y), (x, y1)
                if p1 in self.points and p2 in self.points:
                    count += self.points[p1] * self.points[p2] * c
        return count
                
        
