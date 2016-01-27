__author__ = 'axia'


'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1<=k<=array's length.
'''

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, n):
            if nums[i] < heap[0]:
                continue
            heapq.heapreplace(heap, nums[i])

        return heap[0]

if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,1,5,6,4]
    assert sol.findKthLargest(nums, 2) == 5
    nums = [-1, 2, 0]
    assert sol.findKthLargest(nums, 2) == 0
    nums = [-10, 9, -2, -6, 5, 3, 11, -33, -14, 1, -1, 0]
    assert sol.findKthLargest(nums, 5) == 1