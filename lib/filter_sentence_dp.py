'''
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.
Note:
A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence wont exceed 100.
Length of each word is greater than 0 and wont exceed 10.
1 <= rows, cols <= 20,000.
Example 1:
Input: rows = 2, cols = 8, sentence = ["hello", "world"] Output: 1 Explanation: hello--- world--- The character "-" signifies an empty space on the screen.
Example 2:
Input: rows = 3, cols = 6, sentence = ["a", "bcd", "e"] Output: 2 Explanation: a-bcd- e-a--- bcd-e- The character "-" signifies an empty space on the screen.
Example 3:
Input: rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"] Output: 1 Explanation: I-had apple pie-I had-- The character "-" signifies an empty space on the screen.
'''

class Solution(object):
    def numberOfRepeatence(self, r, c, s):
        if c < len(s[0]):
            return 0
        i = 0  # poistion in r
        j = 0  # position in c
        k = 0  # position in s
        cnt = 0 # cnt
        p = 0 # position of first word
        nr = 0 # number of rows
        memo = {}
        while i < r:
            # print '===', i
            w = s[k]
            while j + len(w) <= c:
                # print '---', j, w
                j += len(w) + 1
                # print '-', j
                if k == 0:
                    if j in memo:
                        i += memo[j][0]
                        j = memo[j][1]
                if k == 
                k = (k+1) % len(s)
                if k == len(s):
                    cnt += 1
                    k = 0
                    memo[p] = [nr, j]
                w = s[k]
            i += 1
            nr += 1
            j = 0
        return cnt

if __name__ == '__main__':
    sol = Solution()
    print sol.numberOfRepeatence(2, 8, ["hello", "world"])
    # assert sol.numberOfRepeatence(2, 8, ["hello", "world"]) is 1
    print sol.numberOfRepeatence(3, 6, ["a", "bcd", "e"])
    print sol.numberOfRepeatence(4, 5, ["I", "had", "apple", "pie"])