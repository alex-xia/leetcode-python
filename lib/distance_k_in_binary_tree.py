'''
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def serialize(self, root):
        tree = []
        queue = [root]
        while len(queue) > 0:
            node = queue[0]
            if node is None:
                tree += [None]
            else:
                tree += [node.val]
                queue += [node.left]
                queue += [node.right]
        return tree

    def listInDistanceForIndex(self, tree, i, k, parent_available):
        # last recursion
        val = tree[i]
        if val is None:
            print '====', i, val
            return []
        if k == 0:
            print '====', i, val
            return [val]

        res = []
        # search left child
        subset = self.listInDistanceForIndex(tree, i * 2 + 1, k - 1, False)
        res += subset
        # search right child
        subset = self.listInDistanceForIndex(tree, i * 2 + 2, k - 1, False)
        res += subset
        # search parent
        if i > 0 and parent_available:
            tree[i] = None
            subset = self.listInDistanceForIndex(tree, (i - 1) / 2, k - 1, True)
            res += subset
        return res


    def listInDistance(self, tree, target, k):
        return self.listInDistanceForIndex(tree, tree.index(target), k, True)

    def distanceK_old(self, root, target, K):
        return self.listInDistance(self.serialize(root), target, K)

    def distanceK(self, root, target, K):
        stack = [root]
        parentMap = {root.val: None}
        while len(stack) > 0:
            node = stack[-1]
            if node.right is not None:
                parentMap[node.right.val] = node
                stack += [node.right]
            if node.left is not None:
                parentMap[node.left.val] = node
                stack += [node.left]
            if node.val == target:
                return self.distanceKFromNode(node, K, parentMap)
        return []

    def distanceKFromNode(self, node, K, parentMap):
        if node is None or node.val is None:
            return []
        if K == 0:
            return [node.val]

        res = []
        v = node.val
        node.val = None
        res += self.distanceKFromNode(node.left, K - 1, parentMap)
        res += self.distanceKFromNode(node.right, K - 1, parentMap)
        res += self.distanceKFromNode(parentMap[v], K - 1, parentMap)
        return res

def array_to_tree(array):
    if len(array) == 0:
        return None
    root = TreeNode(array[0])
    nodearr = [root]
    for i in xrange(1, len(array)):
        v = array[i]
        # print '===', i, v
        if v is not None:
            node = TreeNode(v)
            nodearr += [node]
            pind = (i - 1) / 2
            pnode = nodearr[pind]
            if i % 2 == 0:
                pnode.right = node
            else:
                pnode.left = node
    return root


if __name__ == '__main__':
    sol = Solution()
    # print sol.listInDistance([3,5,1,6,2,0,8,None,None,7,4], 5, 2)
    arr = [3,5,1,6,2,0,8,None,None,7,4]
    root = array_to_tree(arr)
    # print root.val
    print sol.distanceK(root, 5, 2)