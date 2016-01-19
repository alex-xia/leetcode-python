__author__ = 'axia'

'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
'''


import math

def bformat(num):
    return '{0:b}'.format(num)

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        mlen = int(math.floor(math.log(m,2)) + 1)
        nlen = int(math.floor(math.log(n,2)) + 1)
        # print 'm=', bformat(m), 'mlen=', mlen
        # print 'n=', bformat(n), 'nlen=', nlen

        if mlen != nlen:
            return 0

        head = 0
        for i in range(mlen, -1, -1):
            # print 'i->', i
            if i == 0:
                break
            mdigit = (m >> (i-1)) & 1
            ndigit = (n >> (i-1)) & 1
            if mdigit == ndigit:
                head = head * 2 + mdigit
            else:
                break
        #     print 'm>>i-1=', bformat(m >> (i-1))
        #     print 'n>>i-1=', bformat(n >> (i-1))
        # print '<<<<<< i=',i
        return int(head * math.pow(2, i))



if __name__ == '__main__':
    sol = Solution()
    assert sol.rangeBitwiseAnd(5,7) == 4
    assert sol.rangeBitwiseAnd(5,5) == 5