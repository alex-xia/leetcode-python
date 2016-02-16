__author__ = 'axia'
'''
 Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:

"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

'''

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = set()
        self.min = len(s)
        def dfs(i, prefix, score, deleted):
            if deleted > self.min:
                return
            if i == len(s):
                if score == 0:
                    if deleted < self.min:
                        self.min = deleted
                        self.res = {prefix}
                    elif deleted == self.min:
                        self.res.add(prefix)
                return
            c = s[i]
            if c == '(':
                dfs(i+1, prefix+c, score+1, deleted)
                dfs(i+1, prefix, score, deleted + 1)
                return
            if c == ')':
                if score > 0:
                    dfs(i+1, prefix+c, score-1, deleted)
                dfs(i+1, prefix, score, deleted + 1)
                return
            return dfs(i+1,prefix+c,score, deleted)
        dfs(0, '', 0, 0)
        return list(self.res)

if __name__ == '__main__':
    sol = Solution()
    print sol.removeInvalidParentheses('()())()')
    print sol.removeInvalidParentheses('(a)())()')
    print sol.removeInvalidParentheses(')(')