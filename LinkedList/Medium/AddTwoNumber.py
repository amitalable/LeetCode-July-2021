# https://leetcode.com/problems/add-two-numbers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = 0
        curr = root = ListNode()
        while l1 or l2:

            if l1:
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next
            curr.next = ListNode(res % 10)
            curr = curr.next
            res //= 10
        if res:
            curr.next = ListNode(res)
        return root.next
