__author__ = 'axia'

'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''
import math

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hist = set([n])
        while True:
            sum = self.sumSquare(n)
            # print 'sum=', sum
            if sum == 1:
                return True
            if sum in hist:
                return False
            hist.add(sum)
            # print 'hist=', hist
            n = sum
        return False

    def sumSquare(self, n):
        sum = 0
        while n != 0:
            residue = int(n / 10)
            sum += int(math.pow(n % 10, 2))
            n = residue
        return sum

if __name__ == '__main__':
    sol = Solution()
    assert sol.isHappy(19) is True
    assert sol.isHappy(21) is False
    assert sol.isHappy(23) is True

