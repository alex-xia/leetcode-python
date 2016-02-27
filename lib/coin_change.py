__author__ = 'axia'

'''
 You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''


import math

min_depth = None

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        coins = sorted(coins)
        ubound = amount/coins[0] + 1
        self.min_depth = ubound
        self.visited = dict()
        def dfs(coins, amount, depth):
            # print coins, amount, depth, self.min_depth
            i = len(coins) - 1
            while i >= 0 and coins[i] > amount:
                coins.pop()
                i -= 1
            if len(coins) == 0:
                return
            if depth + amount/coins[-1] >= self.min_depth:
                return
            if coins[-1] == amount:
                self.min_depth = min(self.min_depth, depth+1)
                return
            for coin in coins[-1::-1]:
                residue = amount - coin
                if residue not in self.visited or depth + 1 < self.visited[residue]:
                    dfs(coins[:], residue, depth+1)
                    self.visited[residue] = depth + 1

        dfs(coins, amount, 0)
        return -1 if self.min_depth == ubound else self.min_depth

    def coinChange_dp(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        good_coins = []
        for coin in coins:
            if coin == amount:
                return 1
            if coin < amount:
                good_coins.append(coin)
        if len(good_coins) == 0:
            return -1
        coins = good_coins
        dp = [[amount+1] * (amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 0
        for i in range(0, amount+1, coins[0]):
            dp[0][i] = i / coins[0]
        for i in range(1, len(coins)):
            for val in range(1, coins[i]):
                dp[i][val] = dp[i-1][val]
            for val in range(coins[i], amount+1):
                dp[i][val] = min(dp[i-1][val], dp[i][val-coins[i]] + 1)
        res = dp[len(coins)-1][amount]
        return res if res <= amount else -1

    def coinChange_2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse = True)
        lenc, self.res = len(coins), 2**31-1

        def dfs(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (self.res-count): # if hope still exists
                    dfs(i, rem-coins[i], count+1)

        for i in range(lenc):
            dfs(i, amount, 0)
        return self.res if self.res < 2**31-1 else -1


if __name__ == '__main__':
    sol = Solution()
    # coins = [1,2,5]
    # print sol.coinChange(coins,11)
    # coins = [2]
    # print sol.coinChange(coins, 3)
    # coins = [86,210,29,22,402,140,16,466]
    # print sol.coinChange(coins, 3219)
    # coins = [186,419,83,408]
    # print sol.coinChange(coins, 6249)
    # coins = [2]
    # print sol.coinChange(coins, 4)
    # coins = [1,3,5]
    # print sol.coinChange(coins, 8)
    # coins = [58,92,387,421,194,208,231]
    # print sol.coinChange(coins, 7798)
    # coins = [1,2,5]
    # print sol.coinChange(coins, 11)
    print sol.coinChange_dp([227,99,328,299,42,322], 9847)