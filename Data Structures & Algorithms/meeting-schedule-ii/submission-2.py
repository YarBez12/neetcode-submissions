"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: (x.start, x.end))
        h = []
        rooms = 0
        for interval in intervals:
            if not h:
                heapq.heappush(h, interval.end)
                rooms += 1
            elif h[0] <= interval.start:
                heapq.heappop(h)
                heapq.heappush(h, interval.end)
            else:
                rooms += 1
                heapq.heappush(h, interval.end)

        return rooms
        