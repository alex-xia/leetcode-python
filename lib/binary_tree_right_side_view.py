__author__ = 'Qing'

'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        current = [root]
        p = root
        next = []
        while len(current) > 0:
            res.append(p)
            for node in current:
                p = node
                if p.left is not None:
                    next.append(p.left)
                if p.right is not None:
                    next.append(p.right)
            current = next
        return res

