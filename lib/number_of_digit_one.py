__author__ = 'axia'
'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        self.memo = {}
        def count(nd):
            if nd not in self.memo:
                if nd == 0:
                    self.memo[nd] = 0
                else:
                    self.memo[nd] = 10 * count(nd-1) + 10 ** (nd-1)
            return self.memo[nd]

        digit = n % 10
        cnt = 1 if digit >= 1 else 0
        m = n // 10
        nd = 1
        while m > 0:
            res = n - m * (10 ** nd)
            div= m % 10
            cnt += count(nd) * div
            print n, m, div, res, nd, cnt
            if div == 1:
                cnt += res + 1
            elif div > 1:
                cnt += 10 ** nd
            # print 'cnt=', cnt
            m //= 10
            nd += 1

        return cnt

if __name__ == '__main__':
    s = Solution()
    print(s.countDigitOne(11))
