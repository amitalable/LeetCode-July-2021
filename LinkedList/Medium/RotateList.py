# https://leetcode.com/problems/rotate-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getListNodeLength(self, head: ListNode) -> int:
        res = 0
        while head:
            res += 1
            head = head.next
        return res

    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        length = self.getListNodeLength(head)

        if length < 2 or k == length:
            return head

        if k > length:
            k = k % length
        if k == 0:
            return head
        x = length - k-1
        curr = head
        while x:
            curr = curr.next
            x -= 1

        temp = curr.next
        curr.next = None
        ptr = temp
        while ptr.next:
            ptr = ptr.next
        ptr.next = head
        return temp
