__author__ = 'axia'

'''
 Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

Given "abacd", return "dcabacd"

Credits:
'''

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        f = 0
        b = n
        while f < b:
            if self.isPalindrome(s, f, b):
                break
            b -= 1
        res = s
        while b < n:
            res = s[b] + res
            b += 1
        return res



    def isPalindrome(self, s, beg, end):
        f = beg
        b = end - 1
        while f < b:
            if s[f] != s[b]:
                return False
            f += 1
            b -= 1
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestPalindrome('aacecaaa'))
    print(sol.shortestPalindrome('abcd'))