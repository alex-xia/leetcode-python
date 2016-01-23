__author__ = 'Qing'
'''
Count the number of prime numbers less than a non-negative number, n.
'''

import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        isPrime = [True] * n
        for i in range(2):
            isPrime[i] = False
        i = 2
        while i * i < n:
            if isPrime[i]:
                k = i * i
                while k < n:
                    isPrime[k] = False
                    k += i
            i += 1
        cnt = 0
        for i in range(n):
            if isPrime[i]:
                cnt += 1
        return cnt

if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(100))
