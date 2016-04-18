__author__ = 'Qing'
'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
'''

from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        n = len(tickets)
        if n == 0:
            return []
        tickets = sorted(tickets)
        map = defaultdict(list)
        for i, ticket in enumerate(tickets):
            f, t = ticket
            map[f].append(i)
        # print(tickets)
        # print(map)
        def dfs(city, t, m, k):
            print(city, t, m)
            routes = m[city]
            if len(routes) == 0:
                print('return ' + str([city]) if k == len(tickets) else 'return None')
                return [city] if k == len(tickets) else None
            for i, route in enumerate(routes):
                departure, arrival = t[route]
                routes.pop(i)
                rest = dfs(arrival, t, m, k+1)
                if rest is not None:
                    return [departure] + rest
                routes.insert(i, route)
            return None
        return dfs('JFK', tickets, map, 0)

if __name__ == '__main__':
    s = Solution()
    print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
    print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])) #["JFK","NRT","JFK","KUL"]
