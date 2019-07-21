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


# Returns sum of arr[0..index]. This function assumes
# that the array is preprocessed and partial sums of
# array elements are stored in BITree[].
def getsum(BITTree, i):
    s = 0  # initialize result

    # index in BITree[] is 1 more than the index in arr[]
    i = i + 1

    # Traverse ancestors of BITree[index]
    while i > 0:
        # Add current element of BITree to sum
        s += BITTree[i]

        # Move index to parent node in getSum View
        i -= i & (-i)
    return s


# Updates a node in Binary Index Tree (BITree) at given index
# in BITree.  The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.
def updatebit(BITTree, n, i, v):
    # index in BITree[] is 1 more than the index in arr[]
    i += 1

    # Traverse all ancestors and add 'val'
    while i <= n:
        # Add 'val' to current node of BI Tree
        BITTree[i] += v

        # Update index to that of parent in update View
        i += i & (-i)


# Constructs and returns a Binary Indexed Tree for given
# array of size n.
def construct(arr, n):
    # Create and initialize BITree[] as 0
    BITTree = [0] * (n + 1)

    # Store the actual values in BITree[] using update()
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])

    # Uncomment below lines to see contents of BITree[]
    # for i in range(1,n+1):
    #      print BITTree[i],
    return BITTree

LENGTH = 10**9

class RangeModule(object):

    def __init__(self):
        self.bit = construct([], LENGTH)

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        updatebit(self.bit, LENGTH, left, 1)


    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """

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