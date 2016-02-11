__author__ = 'axia'

'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [root]
        pre = None
        cnt = k
        while len(stack) > 0:
            node = stack[-1]
            if not pre or pre.left == node:
                if node.left:
                    stack.append(node.left)
                else:
                    if cnt == 1:
                        return node.val
                    else:
                        stack.pop()
                        cnt -= 1
                    if node.right:
                        stack.append(node.right)
            else:
                if node.left == pre:
                    if cnt == 1:
                        return node.val
                    else:
                        stack.pop()
                        cnt -= 1
                        if node.right:
                            stack.append(node.right)
                elif pre.right == node:
                    if node.left:
                        stack.append(node.left)
                    else:
                        if cnt == 1:
                            return node.val
                        else:
                            stack.pop()
                            cnt -= 1
                        if node.right:
                            stack.append(node.right)
                else:
                    if cnt == 1:
                        return node.val
                    else:
                        stack.pop()
                        cnt -= 1
                    if node.right:
                        stack.append(node.right)
            pre = node
        return None


def array2tree(arr):
    n = len(arr)
    root = TreeNode(arr[0])
    q = [root]
    ind = [0]
    while len(q) > 0:
        node = q.pop(0)
        i = ind.pop(0)
        li = i * 2 + 1
        ri = i * 2 + 2
        if li < n and arr[li]:
            left = TreeNode(arr[li])
            node.left = left
            q.append(left)
            ind.append(li)
        if ri < n and arr[ri]:
            right = TreeNode(arr[ri])
            node.right = right
            q.append(right)
            ind.append(ri)
    return root



if __name__ == '__main__':
    sol = Solution()
    # root = array2tree([4,2,5,1,3])
    # print(sol.kthSmallest(root, 4))
    root = array2tree([1, None, 2])
    print(sol.kthSmallest(root, 2))


