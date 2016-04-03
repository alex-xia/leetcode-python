__author__ = 'Qing'

'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        self.paths = []
        def dfs(i, pre):
            if i < len(path) and path[i] != '/':
                pre += path[i]
                dfs(i+1, pre)
            else:
                if pre == '..':
                    if len(self.paths) > 0:
                        self.paths.pop()
                elif pre and pre != '.':
                    self.paths.append(pre)
                if i < len(path):
                    dfs(i+1, '')
        dfs(0, '')
        return '/' + '/'.join(self.paths)

if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath(''))
    print(s.simplifyPath('/home/'))
    print(s.simplifyPath('/a/./b/../../c/'))
