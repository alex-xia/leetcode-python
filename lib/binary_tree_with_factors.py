'''
* use any language you like
* can google language syntax
* cannot google algorithms or answers : )

Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node's value should be equal to the product of the values of it's children.

How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

Example 1:

Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

[2, 3, 6, 12, 50, 100]

[45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48]
> 777

Note:

1 <= A.length <= 1000.
2 <= A[i] <= 10 ^ 9.
'''


class Solution(object):
    def numFactoredBinaryTrees(self, A):
        A.sort()
        cnts = {x:1 for x in A}
        for i in range(0, len(A)):
            prod = A[i]
            for j in range(0, i+1):
                p = A[j]
                q = prod / p
                # print p, q, prod
                if p * q == prod and q in cnts:
                    cnts[prod] += cnts[p] * cnts[q]
                    # if p != q:
                    #     cnts[prod] += cnts[p] * cnts[q]
                    # print '>>>', cnts
        # print cnts
        return sum(cnts.values()) % (10 ** 9 + 7)

    def numFactoredBinaryTrees_old(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # S = set(A)
        # print 'S=',S
        # self.cnt = len(A)
        # self.bfsNodes(S, A)
        nodeMap = dict()
        for a in A:
            nodeMap[a] = 1
        S = set(A)
        iterations = 0
        while len(S) > 0 and iterations < 10:
            iterations += 1
            next_S = set()
            # print '====', S, nodeMap
            cnt = 0
            for a in S:
                for b in S:
                    if a <= b and a * b in nodeMap:
                        if a == b:
                            nodeMap[a * b] += nodeMap[a]
                        else:
                            nodeMap[a * b] += nodeMap[a] * nodeMap[b] * 2
                        next_S.add(a * b)
                        print '...', a, b, nodeMap
                cnt += 1
                if len(S) == cnt:
                    S = next_S
        # print '>>>>>', nodeMap
        return sum(nodeMap.values())

    # def toMap(self, A, S):
    #     m = {}
    #     for a in A:
    #         for b in A:
    #             if a % b == 0 and a / b in S:
    #                 m[a] = (b, a / b)
    #     return m

    # def toTree(self, C, nodeMap):
    #     next_C = []
    #     for a in C:
    #         for b in C:
    #             if a * b in nodeMap:
    #                 nodeMap[a * b] = nodeMap[a] * nodeMap[b]
    #                 next_C.append(a * b)

    # def bfsNodes(self, S, nodes):
    #     print '====', nodes
    #     if len(nodes) == 0:
    #         return
    #     next_nodes = []
    #     for node in nodes:
    #         for s in S:
    #             if node % s == 0 and node / s in S:
    #                 next_nodes.append(s)
    #                 next_nodes.append(node/s)
    #                 self.cnt += 1
    #     return self.bfsNodes(S, next_nodes)


if __name__ == '__main__':
    s = Solution()
    # print s.numFactoredBinaryTrees([2, 4])
    # print s.numFactoredBinaryTrees([2, 4, 5, 10])
    print s.numFactoredBinaryTrees([2, 4, 8])
    print s.numFactoredBinaryTrees([2, 3, 6])
    print s.numFactoredBinaryTrees([2, 3, 6, 12])
    # print s.numFactoredBinaryTrees([18,3,6,2])
    # print s.numFactoredBinaryTrees([2,3,6,12,18,24,36,218])
    # print s.numFactoredBinaryTrees([45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48])
