__author__ = 'axia'
'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        p, q = 0, 0
        def range_of(p, q):
            return str(nums[p]) if p == q else str(nums[p]) + '->' + str(nums[q])

        while q < len(nums):
            if q == len(nums)-1 or nums[q+1] - nums[q] > 1:
                res.append(range_of(p, q))
                p = q + 1
            q += 1

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.summaryRanges([1, 3, 5, 6]))
    print(s.summaryRanges([0,1,2,4,5,7]))
