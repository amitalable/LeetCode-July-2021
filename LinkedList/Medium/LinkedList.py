from typing import List


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addNode(self, val: int) -> ListNode:
        temp = ListNode(val)
        if self.head is None:
            self.head = temp
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = temp
        return self.head

    def printNode(self) -> List:
        curr = self.head
        listNodes = []
        while curr:
            listNodes.append(curr.val)
            curr = curr.next
        return listNodes


obj = LinkedList()
for i in range(1, 11):
    obj.addNode(i)
print(obj.printNode())
