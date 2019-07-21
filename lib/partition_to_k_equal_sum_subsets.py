'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''

# class Solution(object):
#     def canPartitionKSubsets(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         total = sum(nums)
#         if total % k != 0:
#             return False
#         sorted_nums = sorted(nums)
#         goal = total/k
#         if sorted_nums[-1] > goal:
#             return False
#         while nums[-1] == goal:
#             if len(nums) == 0:
#                 return True
#             nums.pop()
#         return self.canPartitionToGoal(sorted_nums, goal)
#
#     def canPartitionToGoal(self, nums, goal):
#         if len(nums) == 0:
#             return True
#         for i in xrange(0, len(nums)-1):
#             if nums[i]

class Solution(object):
    def __init__(self):
        self.failed = set()

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False
        sorted_nums = sorted(nums)
        goal = total / k
        if sorted_nums[-1] > goal:
            return False
        while sorted_nums[-1] == goal:
            if len(sorted_nums) == 0:
                return True
            sorted_nums.pop()
        return self.canPartitionToGoal(sorted_nums, goal)

    def canPartitionToGoal(self, nums, goal):
        print nums, goal
        if len(nums) == 0:
            return True
        if str(nums) in self.failed:
            return False
        i = 0
        while i < len(nums)-1:
            s = nums[i] + nums[-1]
            if s == goal:
                new_nums = nums[:i] + nums[i + 1:-1]
                if self.canPartitionToGoal(new_nums, goal):
                    return True
                else:
                    self.failed.add(str(new_nums))
            elif s < goal:
                new_nums = nums[:i] + nums[i+1:-1]
                if self.canPartitionToGoal(nums[:i] + nums[i+1:-1] + [s], goal):
                    return True
                else:
                    self.failed.add(str(new_nums))
            else:
                break
            i += 1
        return False

if __name__ == '__main__':
    s = Solution()
    # print s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
    print s.canPartitionKSubsets([4,15,1,1,1,1,3,11,1,10], 3)