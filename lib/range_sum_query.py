__author__ = 'axia'

'''
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''
import math

class BIT:
    def __init__(self, arr):
        self.tree = [0] * (len(arr) + 1)
        self.build(arr)

    def build(self, arr):
        for i in xrange(len(arr)):
            self.add(i, arr[i])

    def add(self, i, val):
        p = i + 1
        while p < len(self.tree):
            self.tree[p] += val
            p += p & -p

    def sum_to(self, i):
        if i < 0:
            return 0
        p = i + 1
        sum = 0
        while p > 0:
            sum += self.tree[p]
            p -= p & -p
        return sum

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.bit = BIT(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.bit.add(i, val-self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.bit.sum_to(j) - self.bit.sum_to(i-1)

class TreeNode(object):
    def __init__(self, val=None, beg=None, end=None):
        self.val = val
        self.beg = beg
        self.end = end
        self.left = None
        self.right = None

class SegmentTree2(object):
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build(nums, 0, len(nums)-1)

    def build(self, nums, beg, end):
        if beg == end:
            return TreeNode(nums[beg], beg, end)
        if beg > end:
            return None
        mid = (end+beg)/2
        left = self.build(nums, beg, mid)
        right = self.build(nums, mid+1, end)
        cur_root = TreeNode(left.val + right.val, left.beg, right.end)
        cur_root.left = left
        cur_root.right = right
        return cur_root

    def update(self, i, val):
        delta = val - self.nums[i]
        self.nums[i] = val
        def dfs(root):
            if i >= root.beg and i <= root.end:
                root.val += delta
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)
        dfs(self.root)

    def sumRange(self, i, j):
        def dfs(root):
            if i==root.beg and j==root.end:
                return root.val
            if i > root.end or j < root.beg:
                return 0
            left = 0
            if root.left:
                left = dfs(root.left)
            right = 0
            if root.right:
                right = dfs(root.right)
            return left + right
        return dfs(self.root)

class SegmentTree(object):
    def __init__(self, nums):
        self.nums = nums
        self.tree = [0] * (2 * (2**int(math.ceil(math.log(len(self.nums),2)))) - 1)
        self.build(0, 0, len(self.nums)-1)

    def build(self, i, beg, end):
        if beg == end:
            self.tree[i] = self.nums[beg]
            return
        if beg > end:
            return
        mid = (beg+end)/2
        self.build(i*2+1, beg, mid)
        self.build(i*2+2, mid+1, end)
        self.tree[i] = self.tree[2*i+1]+self.tree[2*i+2]

    def update(self, i, val):
        delta = val - self.nums[i]
        self.nums[i] = val
        def dfs(pos, beg, end):
            if beg == end:
                if i == beg:
                    self.tree[pos] += delta
                return
            if beg <= i <= end:
                self.tree[pos] += delta
                mid = (beg+end)/2
                dfs(2*pos+1,beg,mid)
                dfs(2*pos+2,mid+1,end)
        dfs(0, 0, len(self.nums)-1)

    def sumRange(self, i, j):
        sum = 0
        def dfs(pos, beg, end):
            if (i == beg and j == end) or beg==end:
                return self.tree[pos]
            if i > end or j < beg:
                return 0
            mid = (beg+end)/2
            return dfs(2*pos+1,beg,mid) + dfs(2*pos+2,mid+1,end)
        return dfs(0, 0, len(self.nums)-1)

class NumArray_segment_tree(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.segment_tree = SegmentTree(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.segment_tree.update(i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.segment_tree.sumRange(i, j)



if __name__ == '__main__':
    # nums = [1,3,5]
    # numArray = NumArray(nums)
    # print numArray.sumRange(0, 2)
    # numArray.update(1, 2)
    # print numArray.sumRange(0, 2)
    # nums = [9,-8]
    # arr = NumArray(nums)
    #
    # # print arr.segment_tree.root.right.val
    # arr.update(0,3)
    # # print arr.segment_tree.tree
    # print arr.sumRange(1,1)
    # print arr.sumRange(0,1)
    # arr.update(1,-3)
    # print arr.sumRange(0,1)
    nums = [0,9,5,7,3]
    arr = NumArray(nums)
    print arr.sumRange(4,4)
    print arr.sumRange(2,4)
    print arr.sumRange(3,3)
    arr.update(4,5)
    arr.update(1,7)
    arr.update(0,8)
    print arr.sumRange(1,2)
    arr.update(1,9)
    print arr.sumRange(4,4)
    arr.update(3,4)