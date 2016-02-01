__author__ = 'axia'

'''
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3.

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.
00000
11111   111111    0 1 2 3 4
10101   010101         1 3
10001   001001      2
10010   000100      3
10011   000010      4
        000001
01234
4 2 1
  2  1
1   1
2   2
3   2
4   3
5   2
6   4
12  6

0 0  0 0  0 0  0  0  0 0
0 0  1 0  0 0  0 -1  0 0

abababc
0012340
odd even odd even
'''

import math

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))

    def bulbSwitch_slow2(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = [2] * n
        cnt[0] = 1
        i = 2
        while i * i <= n:
            j = i
            m = i * j
            while m <= n:
                if j == i:
                    cnt[m-1] += 1
                else:
                    cnt[m-1] += 2
                j += 1
                m = i * j
            i += 1
        print cnt
        return sum(0 if x % 2 == 0 else 1 for x in cnt)

    def bulbSwitch_slow(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        for i in range(n):
            d = self.numOfDividers(i + 1)
            if d % 2 != 0:
                cnt += 1
        return cnt

    def numOfDividers(self, k):
        i = 1
        cnt = 0
        while i * i < k:
            if k % i == 0:
                cnt += 2
            i += 1
        if i * i == k:
            cnt += 1
        return cnt

if __name__ == '__main__':
    sol = Solution()
    print sol.bulbSwitch(5)