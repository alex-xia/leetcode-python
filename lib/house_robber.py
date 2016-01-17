__author__ = 'Qing'

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.rob_begin(nums, 0)

    def rob_begin(self, nums, i):
        if i >= len(nums):
            return 0
        if i == len(nums) - 1:
            return nums[i]
        withi = nums[i] + self.rob_begin(nums, i+2)
        withouti = nums[i+1] + self.rob_begin(nums, i+3)
        return max(withi, withouti)

if __name__ == 'main':
    sol = Solution()
    nums = [2,1,1,2]
    assert sol.rob([nums]) == 4