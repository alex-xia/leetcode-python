__author__ = 'Qing'
'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''

from collections import Counter

class Solution(object):
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        h = s1 + ',' + s2
        if h not in self.memo:
            print(s1, s2)
            if Counter(s1) != Counter(s2):
                print('> False')
                self.memo[h] = False
                return False
            n = len(s1)
            if n <= 3 or s1 == s2:
                print('> True')
                self.memo[h] = True
                return True
            for i in range(1, n):
                if i < n//2 and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                    print('> True')
                    self.memo[h] = True
                    return True
                if i >= n//2 and self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i]):
                    print('> True')
                    self.memo[h] = True
                    return True
                if i < n//2 and self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                    print('> True')
                    self.memo[h] = True
                    return True
                if i >= n//2 and self.isScramble(s1[i:], s2[:n-i]) and self.isScramble(s1[:i], s2[n-i:]):
                    print('> True')
                    self.memo[h] = True
                    return True
            print('> False')
            self.memo[h] = False
            return False
        return self.memo[h]

if __name__ == '__main__':
    s = Solution()
    # print(s.isScramble('great', 'rgtae'))
    # print(s.isScramble('abab', 'bbaa'))
    print(s.isScramble('abcd', 'bcad'))
    # print(s.isScramble("tqxpxeknttgwoppemjkivrulaflayn", "afaylnlurvikjmeppowgttnkexpxqt"))