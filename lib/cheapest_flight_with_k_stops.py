'''
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and fights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
'''

import sys
import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        adj_dict = dict()
        for f in flights:
            dep, arr, price = f[0], f[1], f[2]
            if dep not in adj_dict:
                adj_dict[dep] = dict()
            adj_dict[dep][arr] = price
        if src not in adj_dict:
            return -1
        if K == 0:
            return adj_dict[src][dst]

        pq = []
        for arr in adj_dict[src]:
            price = adj_dict[src][arr]
            heapq.heappush(pq, (price, arr, 0))
        min_cost = sys.maxint
        while len(pq) > 0:
            print pq
            cost, stop, pre_stops = heapq.heappop(pq)
            if pre_stops > K:
                continue
            if cost > min_cost:
                break
            if stop == dst:
                min_cost = min(min_cost, cost)
            if stop not in adj_dict:
                break
            for arr in adj_dict[stop]:
                arr_cost = adj_dict[stop][arr] + cost
                heapq.heappush(pq, (arr_cost, arr, pre_stops+1))
        return -1 if min_cost == sys.maxint else min_cost

if __name__ == '__main__':
    s = Solution()
    # print s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
    # print s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
    # print s.findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1)
    # print s.findCheapestPrice(3, [[0,1,2],[1,2,1],[2,0,10]], 1, 2, 1)
    print s.findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1)
