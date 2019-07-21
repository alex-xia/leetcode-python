'''
A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.
removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).
Example 1:
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
Note:

A half open interval [left, right) denotes all real numbers left <= x < right.
0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
The total number of calls to addRange in a single test case is at most 1000.
The total number of calls to queryRange in a single test case is at most 5000.
The total number of calls to removeRange in a single test case is at most 1000.
'''

class Range(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high


class RangeTreeNode(object):
    def __init__(self, range):
        self.range = range
        self.highest = range.high
        self.left = None
        self.right = None


class RangeModule(object):

    def __init__(self):
        self.rtree = RangeTreeNode(Range(0, 0))


    def addRangeHelper(self, root, range):
        if range.high > root.highest:
            root.highest = range.high

        if range.low == root.low:
            root.range.high = max(root.range.high, range.high)
        elif range.low < root.low:
            if root.left is None:
                root.left = RangeTreeNode(range)
            else:
                self.addRangeHelper(root.left, range)
        else:
            if root.right is None:
                root.right = RangeTreeNode(range)
            else:
                self.addRangeHelper(root.right, range)

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.addRangeHelper(self.rtree, Range(left, right))

    def queryRangeHelper(self, root, range):


    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        if left < self.min or right > self.max:
            return False
        return True

    def removeRangeHelper(self, root, range):
        if root is None:
            return
        if range.high <= root.range.low:
            return self.removeRangeHelper(root.left, range)
        if range.low >= root.range.high:
            return self.removeRangeHelper(root.right, range)
        if range.low > root.range.low and range.high < root.range.high:
            new_range_high = root.range.high
            root.range.high = range.low
            self.addRange(range.high, new_range_high)
            self.removeRangeHelper(root.left, range)
            self.removeRangeHelper(root.right, range)
            return
        if range.low <= root.range.low and range.high >= root.range.high:
            root.range.high = root.range.low
            self.removeRangeHelper(root.left, range)
            self.removeRangeHelper(root.right, range)
            return

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        if left < self.min and right > self.min:
            self.min = right
        if right > self.max and left < self.max:
            self.max = left

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
if __name__ == '__main__':
    obj = RangeModule()
    print obj.min, obj.max
    obj.addRange(10, 20)
    print obj.min, obj.max
    obj.removeRange(14, 16)
    print obj.min, obj.max
    print obj.queryRange(10, 14)
    print obj.queryRange(13, 15)
    print obj.queryRange(16, 17)