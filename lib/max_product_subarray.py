__author__ = 'Qing'

'''
 Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6
'''

import sys

MIN_VALUE = - sys.maxsize - 1

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.res = nums[0]
        def range_product(beg, end):
            if beg == end:
                return None
            pro = 1
            for i in range(beg, end):
                pro *= nums[i]
            return pro

        def max_section(beg, end, neg_first_two, neg_last_two, neg_cnt):
            if neg_cnt % 2 == 0:
                prod = range_product(beg, end)
                if prod is not None:
                    self.res = max(self.res, prod)
                return
            if neg_cnt == 1:
                p = neg_first_two[0]
                left = range_product(beg, p)
                right = range_product(p+1, end)
                if left is not None:
                    self.res = max(self.res, left)
                if right is not None:
                    self.res = max(self.res, right)
                return
            p1, p2 = neg_first_two
            q1, q2 = neg_last_two
            common = range_product(p1+1, q2)
            left = range_product(beg, p1+1)
            right = range_product(q2, end)
            if left is not None:
                self.res = max(self.res, left * common)
            if right is not None:
                self.res = max(self.res, right * common)

        beg = 0
        while beg < len(nums):
            end = beg
            neg_first_two = []
            neg_last_two = []
            neg_cnt = 0
            while end <= len(nums):
                n = nums[end] if end < len(nums) else None
                if n is None or n == 0:
                    if n == 0:
                        self.res = max(self.res, 0)
                    max_section(beg, end, neg_first_two, neg_last_two, neg_cnt)
                    break
                if n < 0:
                    if len(neg_first_two) < 2:
                        neg_first_two.append(end)
                    if len(neg_last_two) == 2:
                        neg_last_two.pop(0)
                    neg_last_two.append(end)
                    neg_cnt += 1
                    end += 1
                    continue
                if n > 0:
                    end += 1
                    continue
            beg = end + 1

        return self.res


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([-99]))              #-99
    print(s.maxProduct([-99, 0]))           #0
    print(s.maxProduct([-99, 1]))           #1
    print(s.maxProduct([-99, -1]))          #99
    print(s.maxProduct([-99, 0, -1]))       #0
    print(s.maxProduct([-99, 1, -1]))       #99
    print(s.maxProduct([2, 3]))             #6
    print(s.maxProduct([-4, -3, -2]))       #12
    print(s.maxProduct([2,-5,-2,-4,3]))     #24