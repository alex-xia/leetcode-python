__author__ = 'Qing'
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.cache = {}
        def dfs(i):
            if i not in self.cache:
                if i == len(s):
                    return 0
                if i == len(s)-1:
                    return 1 if int(s[i]) != 0 else 0
                if i == len(s)-2:
                    if int(s[i]) == 0:
                        return 0
                    if int(s[i+1]) == 0:
                        return 1 if int(s[i]) <= 2 else 0
                    return 1 if int(s[i:i+2]) > 26 else 2
                num = int(s[i])
                if num == 0:
                    return 0
                res = dfs(i+1)
                num = int(s[i:i+2])
                if 10 <= num <= 26:
                    res += dfs(i+2)
                # print(i,res)
                self.cache[i] = res
            return self.cache[i]

        return dfs(0)

if __name__ == '__main__':
    sol = Solution()
    # print(sol.numDecodings('122031'))
    print(sol.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))
