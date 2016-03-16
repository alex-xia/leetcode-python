__author__ = 'Qing'

'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        def get_repeat_len(s, beg):
            cnt = 1
            for i in range(beg+1, len(s)):
                if s[i] == s[i-1]:
                    cnt += 1
                else:
                    break
            return cnt

        def dfs(i,j):
            print(i,j,s1[:i],s2[:j],s3[:i+j])
            if i == len(s1) and j == len(s2):
                return i+j == len(s3)
            if i == len(s1):
                return s2[j:] == s3[i+j:]
            if j == len(s2):
                return s1[i:] == s3[i+j:]
            if s1[i] == s2[j] == s3[i+j]:
                n1 = get_repeat_len(s1, i)
                n2 = get_repeat_len(s2, j)
                n3 = get_repeat_len(s3, i+j)
                print(n1,n2,n3)
                if n1+n2 < n3:
                    return False
                if n1 > n3 and n2 > n3:
                    return False
                if n1 <= n3 and n2 <= n3:
                    return dfs(i+n1, j) or dfs(i, j+n2)
                elif n1 <= n3:
                    return dfs(i+n1, j)
                else:
                    return dfs(i, j+n2)
            if s1[i] == s3[i+j]:
                if dfs(i+1, j):
                    return True
            if s2[j] == s3[i+j]:
                if dfs(i, j+1):
                    return True
            return False
        return dfs(0,0)

if __name__ == '__main__':
    s = Solution()
    # print(s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
    # print(s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
    # s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    # s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    # s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    # print(s.isInterleave(s1,s2,s3))
    print(s.isInterleave('aa','ab','aaba'))
    print(s.isInterleave("aabc", "abad", "aabcabad"))