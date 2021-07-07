# https://leetcode.com/problems/subtree-of-another-tree/

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isIdentical(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)

    def isSubtreeUsingRecursion(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return False
        if self.isIdentical(root1, root2):
            return True
        # If not identical check the subtree of the current node
        return self.isSubtree(root1.left, root2) or self.isSubtree(root1.right, root2)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        queue1 = deque([root])
        queue2 = deque([subRoot])
        tempRootCandidates = []

        # Walk through tree to find start of subroot
        while queue1:
            for i in range(len(queue1)):
                cur = queue1.popleft()
                if cur.val == subRoot.val:
                    # There might be multiple curr node equals to subroot node
                    # So we shouldn't break it right away.
                    tempRootCandidates.append(cur)
                if cur.left:
                    queue1.append(cur.left)
                if cur.right:
                    queue1.append(cur.right)
        # Walked through tree and cannot find subRoot
        if not tempRootCandidates:
            return False

        # Walk through remaining nodes to see if matches subtree
        for candidate in tempRootCandidates:
            queue1.append(candidate)
            found = True
            while queue1 and queue2:
                for i in range(len(queue1)):
                    cur1 = queue1.popleft()
                    cur2 = queue2.popleft()

                    if cur1.val != cur2.val:
                        found = False
                        break

                    if cur1.left or cur2.left:
                        if not cur1.left or not cur2.left:
                            found = False
                            break
                        else:
                            queue1.append(cur1.left)
                            queue2.append(cur2.left)
                    if cur1.right or cur2.right:
                        if not cur1.right or not cur2.right:
                            found = False
                            break
                        else:
                            queue1.append(cur1.right)
                            queue2.append(cur2.right)
            if found:
                return True
        return False
