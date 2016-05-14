__author__ = 'Qing'
'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def pre_traverse(self, root):
        if root is None:
            return [0]
        res = [root.val]
        if root.left:
            lc = self.pre_traverse(root.left)
            res.append(len(lc))
            res.extend(lc)
        else:
            res.append(0)
        if root.right:
            res.extend(self.pre_traverse(root.right))
        return res


    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return ','.join([str(x) for x in self.pre_traverse(root)])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nums = [int(x) for x in data.split(',')]
        if len(nums) == 1:
            return None
        print(nums)
        def des(root, lp, nl, rp, nr):
            print(root.val, lp, nl, rp, nr)
            if nl > 0:
                lroot = TreeNode(nums[lp])
                lnl = nums[lp+1]
                root.left = des(lroot, lp+2, lnl, lp+2+lnl, nl-2-lnl)
            if nr > 0:
                rroot = TreeNode(nums[rp])
                rnl = nums[rp+1]
                root.right = des(rroot, rp+2, rnl, rp+2+rnl, nr-2-rnl)
            return root

        root = TreeNode(nums[0])
        lp = 2
        nl = nums[1]
        return des(root, lp, nl, lp+nl, len(nums)-2-nl)

if __name__ == '__main__':
    c = Codec()
    root = c.deserialize('1,2,2,0,3,4,4,2,6,0,5,0')
    print(c.serialize(root))
    print(root.right.left.left.val)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))