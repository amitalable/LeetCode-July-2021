# https://leetcode.com/problems/symmetric-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        leftStack, rightStack = [root.left], [root.right]
        while leftStack and rightStack:
            x, y = leftStack.pop(0), rightStack.pop(0)
            if x and y:
                if x.val == y.val:
                    leftStack.append(x.left)
                    rightStack.append(y.right)
                    leftStack.append(x.right)
                    rightStack.append(y.left)
                else:
                    return False
            elif (x and not y) or (not x and y):
                return False
        return True

    def isSymmetricUsingRecursion(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        return (t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)

    def insert(self, l):
        root = None
        if l:
            root = TreeNode(l.pop(0))
            stack = [root]
            while l:
                # if there is only left node in l
                y = stack.pop(0)
                left = l.pop(0)
                y.left = TreeNode(left) if left else None
                if len(l) > 0:
                    right = l.pop(0)
                    y.right = TreeNode(right) if right else None
                    stack.append(y.left)
                    stack.append(y.right)
        return root


# [9,-42,-42,null,76,76,null,null,13,null,13]
root = TreeNode(9)
root.left = TreeNode(-42)
root.left.left = None
root.left.right = TreeNode(76)

root.right = TreeNode(-42)
root.right.left = TreeNode(76)
root.right.right = None


obj = Solution()
root1 = obj.insert([9, -42, -42, None, 76, 76, None])
print(obj.isSymmetric(root))
print(obj.isSymmetricUsingRecursion(root1))
