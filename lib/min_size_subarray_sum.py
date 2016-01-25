__author__ = 'Qing'

'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        head = 0
        tail = 0
        sum = 0
        n = len(nums)
        m = n + 1
        while tail < n:
            sum += nums[tail]
            while sum >= s:
                m = min(m, tail - head + 1)
                sum -= nums[head]
                head += 1
            tail += 1
        if m == n + 1:
            return 0
        return m

if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
    print(sol.minSubArrayLen(15, [1,2,3,4,5]))