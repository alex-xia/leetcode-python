'''
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        q = [(0, root)]
        i = 0
        row_max = 0
        pre_row = -1
        while len(q) > i:
            n = q[i]
            i += 1
            cur_row, cur_node = n[0], n[1]
            if cur_row > pre_row:
                if pre_row > -1:
                    res.append(row_max)
                row_max = cur_node.val
            else:
                row_max = max(row_max, cur_node.val)
            pre_row = cur_row
            if cur_node.left is not None:
                q.append((cur_row+1, cur_node.left))
            if cur_node.right is not None:
                q.append((cur_row+1, cur_node.right))
        res.append(row_max)
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
    s = Solution()
    arr = [1,3,2,5,3,None,9]
    root = array_to_tree(arr)
    # print root.val
    print s.largestValues(root)