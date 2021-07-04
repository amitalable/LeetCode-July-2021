# https://leetcode.com/problems/same-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTreeUsingRecursion(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p and q or p and not q:
            return False

        return self.isSameTree(p.left, q.left) \
            and p.val == q.val and \
            self.isSameTree(p.right, q.right)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack1, stack2 = [p], [q]
        while stack1 and stack2:
            p = stack1.pop(0)
            q = stack2.pop(0)
            if p and q:
                if p.val != q.val:
                    return False
                stack1.append(p.left)
                stack2.append(q.left)
                stack1.append(p.right)
                stack2.append(q.right)
            elif not p and q or p and not q:
                return False
        return True


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node1 = TreeNode(1)
node1.left = TreeNode(9)
node1.right = TreeNode(3)
print(Solution().isSameTree(node, node1))
