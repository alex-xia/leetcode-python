__author__ = 'axia'

class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root if root else None

    def from_list(self, arr):
        if len(arr) == 0:
            return None
        def build(i):
            if i >= len(arr):
                return None
            if arr[i] is None:
                return None
            node = TreeNode(arr[i])
            node.left = build(i*2+1)
            node.right = build(i*2+2)
            return node
        return build(0)

    def to_list(self):
        res = [self.root]
        def add(pre):
            nxt = len(res)
            for i in xrange(pre, nxt):
                if res[i].left:
                    res.append(res[i].left)
                if res[i].right:
                    res.append(res[i].right)
            if len(res) > nxt:
                add(nxt)
        add(0)
        return [x.val for x in res]

    def post_order(self, root=None):
        root = self.root if not root else root
        pre = None
        stack = [root]
        res = []
        while len(stack) > 0:
            p = stack[-1]
            if not pre or pre.left == p or pre.right == p:
                if p.left:
                    stack.append(p.left)
                elif p.right:
                    stack.append(p.right)
                else:
                    stack.pop()
                    res.append(p.val)
            elif p.left == pre:
                if p.right:
                    stack.append(p.right)
                else:
                    stack.pop()
                    res.append(p.val)
            elif p.right == pre:
                stack.pop()
                res.append(p.val)
            pre = p
        return res

    def post_order_recursive(self, root=None):
        root = self.root if not root else root
        res = []
        if not root:
            return []
        if root.left:
            res = self.post_order_recursive(root.left)
        if root.right:
            res.extend(self.post_order_recursive(root.right))
        res.append(root.val)
        return res


    def pre_order(self, root=None):
        root = self.root if not root else root
        res = []
        stack = [root]
        while len(stack) > 0:
            p = stack.pop()
            res.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        return res

    def pre_order_recursive(self, root=None):
        root = self.root if not root else root
        res = []
        res.append(root.val)
        if root.left:
            res.extend(self.pre_order_recursive(root.left))
        if root.right:
            res.extend(self.pre_order_recursive(root.right))
        return res

    def in_order(self, root=None):
        root = self.root if not root else root
        stack = [root]
        res = []
        pre = None
        while len(stack) > 0:
            p = stack[-1]
            if not pre or pre.left == p or pre.right == p:
                if p.left:
                    stack.append(p.left)
                else:
                    stack.pop()
                    res.append(p.val)
                    if p.right:
                        stack.append(p.right)
            else:
                stack.pop()
                res.append(p.val)
                if p.right:
                    stack.append(p.right)
            pre = p
        return res

    def in_order_recursive(self, root=None):
        root = self.root if not root else root
        res = []
        if not root:
            return res
        if root.left:
            res = self.in_order_recursive(root.left)
        res.append(root.val)
        if root.right:
            res.extend(self.in_order_recursive(root.right))
        return res




if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = bt.from_list([1,2,3,4,5])
    print bt.to_list()
    print bt.post_order()
    print bt.post_order_recursive()
    print bt.pre_order()
    print bt.pre_order_recursive()
    print bt.in_order()
    print bt.in_order_recursive()