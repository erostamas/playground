import math

import heapq

class MedianFinder:
    def __init__(self):
        # max heap for lower half (store negative values)
        self.low = []
        # min heap for upper half
        self.high = []

    def add_num(self, num: int) -> None:
        # Push to max heap (invert sign for max heap behavior)
        heapq.heappush(self.low, -num)
        
        # Balance heaps so every number in low <= every number in high
        if self.low and self.high and (-self.low[0]) > self.high[0]:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        
        # Keep sizes balanced or low has 1 more element
        if len(self.low) > len(self.high) + 1:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        elif len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)

    def find_median(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0


mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
print(mf.find_median())  # Output: 1.5
mf.add_num(3)
print(mf.find_median())  # Output: 2