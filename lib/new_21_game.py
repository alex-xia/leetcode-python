'''
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.
During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.
Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
Note:

0 <= K <= N <= 10000class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.
'''

def series_sum(n):
    return n * (n+1) / 2

class Solution(object):
    def __init__(self):
        self.memo = dict()

    def combinations2S(self, W, S):
        if S in self.memo:
            return self.memo[S]
        combinations = 0
        if S == 0:
            return 1
        for i in xrange(1, min(W+1, S+1)):
            combinations += self.combinations2S(W, S-i)
        self.memo[S] = combinations
        # print S, combinations
        return combinations

    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        print 'N=', N, 'K=', K, 'W=', W
        if K == 0:
            return float(N == 0)

        S = max(N - W + 1, 0)
        print 'S=', S
        bad_combinations = 0
        i = S + W - N
        for c in xrange(S, K):
            print '=====', c, i
            bad_combinations += self.combinations2S(W, c) * i
            i += 1
        M = K - W
        print 'M=', M
        total_combinations = 0
        i = K - M - W + 1
        for c in xrange(M, K):
            if c >= 0 and i > 0:
                print '>>>>>', c, i
                total_combinations += self.combinations2S(W, c) * i
            i += 1
        return 1 - 1.0 * bad_combinations / total_combinations


if __name__ == '__main__':
    s = Solution()
    # print s.combinations2S(3, 4)
    print s.new21Game(21, 17, 10)
    # print s.new21Game(10, 1, 10)
    # print s.new21Game(6, 1, 10)