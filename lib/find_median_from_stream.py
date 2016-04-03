__author__ = 'Qing'

'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
'''

from heapq import heappush, heappop, heapreplace

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.smaller = []
        self.larger = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.smaller) <= len(self.larger):
            if len(self.larger) > 0 and num > self.larger[0]:
                num = heapreplace(self.larger, num)
            heappush(self.smaller, -num)
        else:
            if num < -self.smaller[0]:
                num = -heapreplace(self.smaller, -num)
            heappush(self.larger, num)
        print(self.smaller, self.larger)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.smaller) == len(self.larger):
            return (-self.smaller[0] + self.larger[0]) / 2.0
        else:
            return -self.smaller[0]*1.0

# Your MedianFinder object will be instantiated and called as such:
if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(2)
    print(mf.findMedian())
    mf.addNum(3)
    # mf.addNum(2)
    # mf.addNum(5)
    print(mf.findMedian())