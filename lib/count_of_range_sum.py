__author__ = 'axia'
'''
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i <= j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
'''
import bisect

class BIT:
    def __init__(self, length):
        self.tree = [0] * length

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

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        So fxxking concise !!!!!!!!!!!
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return int(lower <= nums[0] <= upper)
        mid = len(nums) >> 1
        count = sum([
            self.countRangeSum(array, lower, upper)
            for array in [nums[:mid], nums[mid:]]
        ])

        suffix, prefix = [0] * (mid+1), [0] * (len(nums)-mid+1)
        for i in xrange(mid-1, -1, -1):
            suffix[i] += suffix[i+1] + nums[i]
        for i in xrange(mid, len(nums)):
            prefix[i-mid+1] += prefix[i-mid] + nums[i]
        suffix, prefix = suffix[:-1], sorted(prefix[1:])
        count += sum([
            bisect.bisect_right(prefix, upper-left) -
            bisect.bisect_left(prefix, lower-left)
            for left in suffix
        ])
        return count

    def countRangeSum_bit(self, nums, lower, upper):
        """
        So fxxking concise !!!!!!!!!!!
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        def cumsum(arr):
            res = [0] * (len(arr) + 1)
            for i in range(len(arr)):
                res[i+1] = res[i] + arr[i]
            return res
        cum_sum = cumsum(nums)
        # print cum_sum
        cand = []
        for cs in cum_sum:
            cand.append(cs)
            cand.append(cs+lower-1)
            cand.append(cs+upper)
        # print 'before sorting:', cand
        cand = sorted(cand)
        # ghost = [0] * len(cand)
        # print 'after sorting:', cand
        bit = BIT(len(cand) + 1)
        for cs in cum_sum:
            bit.add(bisect.bisect_left(cand, cs), 1)
            # ghost[cand.index(cs)] += 1
        # print '>>>>>>> ghost =', ghost
        cnt = 0
        for cs in cum_sum:
            # print 'cs =', cs
            bit.add(bisect.bisect_left(cand, cs), -1)
            # ghost[cand.index(cs)] -= 1
            # print '<<<<<<< ghost =', ghost
            cnt += bit.sum_to(bisect.bisect_left(cand, cs+upper))
            cnt -= bit.sum_to(bisect.bisect_left(cand, cs+lower-1))
        return cnt

if __name__ == '__main__':
    s = Solution()
    print s.countRangeSum_bit([-2,5,-1],-2,2)