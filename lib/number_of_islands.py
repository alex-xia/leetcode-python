__author__ = 'Qing'

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

class Solution(object):
    def __init__(self):
        self.nr = None
        self.nc = None

    def rc2ind(self, r, c):
        return r * self.nc + c

    def isInside(self, r, c):
        return r >= 0 and r < self.nr and c >= 0 and c < self.nc

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.nr = len(grid)
        if self.nr == 0:
            return 0
        self.nc = len(grid[0])
        ones = dict()
        for i in range(self.nr):
            for j in range(self.nc):
                if grid[i][j] == '1':
                    k = self.rc2ind(i, j)
                    ones[k] = [i,j]
        cnt = 0
        while len(ones) > 0:
            cnt += 1
            k, ij = ones.popitem()
            stack = [ij]
            while len(stack) > 0:
                [i, j] = stack.pop()
                for [r, c] in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if self.isInside(r,c) and grid[r][c] == '1':
                        k = self.rc2ind(r, c)
                        if k in ones:
                            del ones[k]
                            stack.append([r, c])
        return cnt

if __name__ == '__main__':
    sol = Solution()
    grid = ['11000',
            '11000',
            '00100',
            '00011']
    print(sol.numIslands(grid))
    grid = ['1']
    print(sol.numIslands(grid))



