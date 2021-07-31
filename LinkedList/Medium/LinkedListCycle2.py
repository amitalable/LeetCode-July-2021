# https://leetcode.com/problems/linked-list-cycle-ii

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # UsingFloydsCycleDetectionAlgorithm
        tortoise = hare = head
        while tortoise and hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                break

        if tortoise is None or hare is None or hare.next is None:
            return None

        tortoise = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
        return tortoise


node = ListNode(1)
temp = node.next = ListNode(3)
node.next.next = ListNode(2)
node.next.next.next = ListNode(5)
node.next.next.next.next = temp

obj = Solution()
res = obj.detectCycle(node)
print(res)
