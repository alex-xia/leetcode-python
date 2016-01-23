__author__ = 'Qing'

'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
'''

class Solution(object):
    def isIsomorphic_slow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lookup = dict()
        n = len(s)
        for i in range(n):
            c = s[i]
            if c in lookup:
                lookup[c].append(i)
            else:
                lookup[c] = [i]
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            c = s[i]
            d = t[i]
            ci = lookup[c]
            if len(ci) > 1:
                for j in range(1,len(ci)):
                    k = ci[j]
                    if t[k] != d:
                        return False
                    visited[j] = True
        return True
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_lookup = dict()
        t_lookup = dict()
        n = len(s)
        for i in range(n):
            sc = s[i]
            tc = t[i]
            if sc in s_lookup:
                p = s_lookup[sc]
                if tc != t[p]:
                    return False
            else:
                s_lookup[sc] = i
                if tc in t_lookup:
                    p = t_lookup[tc]
                    if sc != s[p]:
                        return False
                else:
                    t_lookup[tc] = i
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic('aba','cdc'))
    assert sol.isIsomorphic('aba','cdc') == True
    print(sol.isIsomorphic('aba','cdd'))
    assert sol.isIsomorphic('aba','cdd') == False
    print(sol.isIsomorphic('aba','ccc'))
    assert sol.isIsomorphic('aba','ccc') == False