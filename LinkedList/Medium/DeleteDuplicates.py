# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0, head)
        pred = sentinel
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next
        return sentinel.next

    def printNode(self, head):
        listNode = []
        while head:
            listNode.append(head.val)
            head = head.next
        return listNode

    def addNodes(self):
        ptr = node = ListNode(0)
        for i in 1, 1, 1, 2, 3:
            ptr.next = ListNode(i)
            ptr = ptr.next
        return node.next


obj = Solution()
nodes = obj.addNodes()
deleteDuplicates = obj.deleteDuplicates(nodes)
print(obj.printNode(deleteDuplicates))
