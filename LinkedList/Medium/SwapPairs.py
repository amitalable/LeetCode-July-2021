# https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        ptr = ptr1 = ListNode()
        curr = ptr1.next = head
        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            ptr1.next = temp
            ptr1 = curr
            curr = curr.next
        return ptr.next

    def swapPairsUsingRecursion(self, head: ListNode) -> ListNode:

        def swapPair(head):
            if head is None or head.next is None:
                return head

            cur = head
            nextnode = head.next
            nextnextnode = nextnode.next

            # swap
            nextnode.next = cur
            nextPairHead = swapPair(nextnextnode)

            cur.next = nextPairHead

            return nextnode

        return swapPair(head)
