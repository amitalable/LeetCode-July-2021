# https://leetcode.com/problems/partition-list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return
        a = aHead = ListNode()
        b = bHead = ListNode()
        cur = head
        while cur:
            if cur.val < x:
                a.next = cur
                a = cur
            else:
                b.next = cur
                b = cur
            cur = cur.next
        a.next = bHead.next
        b.next = None
        return aHead.next

    def addNodes(self):
        ptr = node = ListNode(0)
        for i in 1, 4, 3, 2, 5, 2:
            ptr.next = ListNode(i)
            ptr = ptr.next
        return node.next

    def printNode(self, head):
        listNode = []
        while head:
            listNode.append(head.val)
            head = head.next
        return listNode


obj = Solution()
head = obj.addNodes()
partition = obj.partition(head, 3)
print(obj.printNode(partition))
