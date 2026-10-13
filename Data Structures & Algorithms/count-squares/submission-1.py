class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        seen = set()
        for p, c in self.points.items():
            x1, y1 = p
            if x1 == x and y1 == y:
                continue
            dx = x1 - x
            dy = y1 - y


            if dx == 0:
                p1, p2 = (x-dy, y), (x1-dy,y1)
                count += self.check(p1, p2, c, seen)
                p1, p2 = (x+dy, y), (x1+dy,y1)
                count += self.check(p1, p2, c, seen)



            if dy == 0:
                p1, p2 = (x, y-dx), (x1,y1-dx)
                count += self.check(p1, p2, c, seen)
                p1, p2 = (x, y+dx), (x1,y1+dx)
                count += self.check(p1, p2, c, seen)
            

            if abs(dx) == abs(dy):
                p1, p2 = (x1, y), (x, y1)
                count += self.check(p1, p2, c, seen)
            

            seen.add(p)
        return count
    
    def check(self, p1, p2, c, seen):
        if p1 in self.points and p2 in self.points and p1 not in seen and p2 not in seen:
                    return self.points[p1] * self.points[p2] * c
        return 0

                
        
