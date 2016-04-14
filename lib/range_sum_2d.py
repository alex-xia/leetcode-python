__author__ = 'Qing'

'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:

    You may assume that the matrix does not change.
    There are many calls to sumRegion function.
    You may assume that row1 ≤ row2 and col1 ≤ col2.

'''
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        nr = len(matrix)
        if nr == 0:
            self.matrix = None
            return
        nc = len(matrix[0])
        self.memo = [[-1] * nc for _ in range(nr)]
        for r in range(nr):
            for c in range(nc):
                self.memo[r][c] = self.top_left_sum(r, c)

    def top_left_sum(self, row, col):
        val = self.matrix[row][col]
        if row == 0 and col == 0:
            return val
        if row == 0:
            return val + self.memo[row][col-1]
        if col == 0:
            return val + self.memo[row-1][col]
        return val + self.memo[row][col-1] + self.memo[row-1][col] - self.memo[row-1][col-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.matrix is None:
            return 0
        sum = self.memo[row2][col2]
        if row1 == 0 and col1 == 0:
            return sum
        if row1 == 0:
            return sum - self.memo[row2][col1-1]
        if col1 == 0:
            return sum - self.memo[row1-1][col2]
        return sum - self.memo[row2][col1-1] - self.memo[row1-1][col2] + self.memo[row1-1][col1-1]


if __name__ == '__main__':
    m = NumMatrix([
                      [3, 0, 1, 4, 2],
                      [5, 6, 3, 2, 1],
                      [1, 2, 0, 1, 5],
                      [4, 1, 0, 1, 7],
                      [1, 0, 3, 0, 5]
                    ])
    print(m.sumRegion(2, 1, 4, 3))
    print(m.sumRegion(1, 1, 2, 2))

