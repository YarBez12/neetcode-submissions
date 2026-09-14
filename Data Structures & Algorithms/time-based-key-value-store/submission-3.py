class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        if not values or values[0][0] > timestamp:
            return "" 
        ind = self.binarySearch(values, timestamp)
        return values[ind][1]

    def binarySearch(self, values, timestamp):
        l = 0
        r = len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1

        return r
        
