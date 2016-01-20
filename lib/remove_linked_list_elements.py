__author__ = 'axia'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        node = self
        output = ''
        while node is not None:
            output += '->' + str(node.val)
            node = node.next
        return output

class SolutionRecursive(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        print 'current list = ', head
        if head is None:
            return None
        if head.val == val:
            return self.removeElements(head.next, val)
        next = self.removeElements(head.next, val)
        head.next = next
        return head

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        pre_head = ListNode(0)
        cur = pre_head
        cur.next = head
        nxt = head
        while True:
            while nxt is not None and nxt.val == val:
                nxt = nxt.next
            if nxt is None:
                cur.next = None
                break
            cur.next = nxt
            cur = nxt
            nxt = cur.next
        return pre_head.next



if __name__ == '__main__':
    head = ListNode(5)
    node = ListNode(9)
    head.next = node
    for i in range(5):
        node.next = ListNode(9)
        node = node.next
    node.next = ListNode(9)
    print head
    sol = Solution()
    print sol.removeElements(head, 9)
