__author__ = 'axia'
'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        p, q = 0, len(s)-1
        while p < q:
            s[p], s[q] = s[q], s[p]
            p += 1
            q -= 1
        return ''.join(s)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseString('hello world'))