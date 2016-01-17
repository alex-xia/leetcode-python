__author__ = 'Qing'

'''
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            cnt += 1
            n &= (n-1)
        return cnt


if __name__ == 'main':
    solution = Solution()
    assert solution.hammingWeight(11) == 3