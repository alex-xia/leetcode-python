__author__ = 'Qing'

'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        nr = len(board)
        if nr == 0:
            return word == ''
        nc = len(board[0])

        def hash(i, j):
            return str(i) + '#' + str(j)

        def hash2(i, j, k):
            return str(i) + '#' + str(j) + '#' + str(k)

        def dfs(i, j, k, visited):
            h = hash2(i, j, k)

            letter = word[k]
            nxt_visited = set(visited)
            nxt_visited.add(hash(i, j))
            if board[i][j] != letter:
                return False
            for (r, c) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if k == len(word) - 1:
                    return True

                if hash(r, c) not in visited and 0 <= r < nr and 0 <= c < nc and dfs(r, c, k+1, nxt_visited):
                    return True
            return False

        for p in range(nr):
            for q in range(nc):
                if board[p][q] == word[0] and dfs(p, q, 0, set()):
                    return True
        return False

if __name__ == '__main__':
    s = Solution()
    # print(s.exist(["ABCE",
    #                "SFES",
    #                "ADEE"], 'ABCESEEEFS'))
    board = [
              ['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']
            ]
    print(s.exist(board, 'ABCB'))
    board = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaab"]
    print(s.exist(board,"baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
