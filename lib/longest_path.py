__author__ = 'axia'

'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''

def printm(m):
    for row in m:
        print(row)

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        r = len(matrix)
        if r == 0:
            return 0
        c = len(matrix[0])
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i-1, j) if i > 0 and val > matrix[i-1][j] else 0,
                    dfs(i+1, j) if i < r - 1 and val > matrix[i+1][j] else 0,
                    dfs(i, j-1) if j > 0 and val > matrix[i][j-1] else 0,
                    dfs(i, j+1) if j < c - 1 and val > matrix[i][j+1] else 0
                )
            return dp[i][j]
        dp = [[0] * c for _ in range(r)]
        return max(dfs(i,j) for i in range(r) for j in range(c))



if __name__ == '__main__':
    sol = Solution()
    nums = [
              [9,9,4],
              [6,6,8],
              [2,1,1]
            ]
    print(sol.longestIncreasingPath(nums))

    nums = [
              [3,4,5],
              [3,2,6],
              [2,2,1]
            ]
    print(sol.longestIncreasingPath(nums))

    nums = [[7,8,9],
            [9,7,6],
            [7,2,3]]
    print(sol.longestIncreasingPath(nums))