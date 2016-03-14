__author__ = 'axia'
'''
 Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
'''
from tree_traverse import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        pre_traverse, pre_output = None, None
        stack = [root]
        while len(stack) > 0:
            node = stack[-1]
            print '<<<<', node.val, pre_traverse.val if pre_traverse is not None else 'None'
            if pre_traverse is None or pre_traverse.left == node or pre_traverse.right == node:
                if node.left is None:
                    stack.pop()
                    if pre_output is not None and node.val <= pre_output.val:
                        return False
                    pre_output = node
                    if node.right:
                        stack.append(node.right)
                else:
                    stack.append(node.left)
            else:
                stack.pop()
                if pre_output is not None and node.val <= pre_output.val:
                    return False
                pre_output = node
                if node.right:
                    stack.append(node.right)
            pre_traverse = node
            print '>>>>', [x.val for x in stack]
            print pre_output.val if pre_output is not None else 'None'
        return True

    def isValidBST_recursion(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.pre_output = None
        def in_order_check(node):
            if self.is_leaf(node):
                if self.pre_output is not None and node.val <= self.pre_output.val:
                    return False
                self.pre_output = node
                return True
            if node.left:
                if not in_order_check(node.left):
                    return False
            if self.pre_output is not None and node.val <= self.pre_output.val:
                return False
            self.pre_output = node
            if node.right:
                if not in_order_check(node.right):
                    return False
            return True
        return in_order_check(root)

    @staticmethod
    def is_leaf(node):
        assert node is not None
        return node.left is None and node.right is None

if __name__ == '__main__':
    s = Solution()
    bt = BinaryTree()
    bt.root = bt.from_list([5,3,8,2,4,7,11, None, None, None, None, None, None, 9])
    print s.isValidBST_recursion(bt.root)
    bt.root = bt.from_list([1,2,3,4,5,6])
    print s.isValidBST_recursion(bt.root)