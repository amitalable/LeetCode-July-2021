# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 1
        cur = ptr = head
        while cur.next:
            size += 1
            cur = cur.next
            if size > n + 1:
                ptr = ptr.next
        if size == n:
            return head.next
        ptr.next = ptr.next.next
        return head
