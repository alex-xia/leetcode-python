__author__ = 'Qing'

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution(object):
    def __init__(self):
        self.cache = dict()
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.rob_begin(nums, 0)

    def rob_begin(self, nums, i):
        if(i in self.cache):
            return self.cache[i]
        if i >= len(nums):
            return 0
        if i == len(nums) - 1:
            return nums[i]
        withi = nums[i] + self.rob_begin(nums, i+2)
        withouti = nums[i+1] + self.rob_begin(nums, i+3)
        res = max(withi, withouti)
        self.cache[i] = res
        return res

if __name__ == '__main__':
    sol = Solution()
    nums = [2,1,1,2]
    assert sol.rob(nums) == 4
    sol = Solution()
    nums = [155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]
    assert sol.rob(nums) == 4517