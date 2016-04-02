__author__ = 'axia'
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        def to_char(k):
            return chr(ord('A') + k - 1)

        title = ''
        upper = (n-1) // 26
        lower = n - upper * 26
        while upper > 0:
            title = to_char(lower) + title
            n = upper
            upper = (n-1) // 26
            lower = n - upper * 26

        title = to_char(lower) + title
        return title

if __name__ == '__main__':
    s = Solution()
    print([s.convertToTitle(x) for x in [24, 26, 27, 100]])
