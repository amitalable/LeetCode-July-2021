# https://leetcode.com/problems/range-sum-of-bst

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root]
        res = 0
        while stack:
            curr = stack.pop(0)
            if curr:
                if curr.val < low:
                    stack.append(curr.right)
                elif curr.val > high:
                    stack.append(curr.left)
                else:
                    res += curr.val
                    stack.append(curr.left)
                    stack.append(curr.right)
        return res

    def rangeSumBSTUsingRecursion(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            if root.val < low:
                return self.rangeSumBSTUsingRecursion(root.right, low, high)
            if root.val > high:
                return self.rangeSumBSTUsingRecursion(root.left, low, high)
            return root.val +\
                self.rangeSumBSTUsingRecursion(root.left, low, high) +\
                self.rangeSumBSTUsingRecursion(root.right, low, high)
        return 0

    def insert(self, l: TreeNode) -> TreeNode:
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


root = [10, 5, 15, 3, 7, 13, 18, 1, None, 6]  # [10, 5, 15, 3, 7, None, 18]
low = 6  # 7
high = 10  # 15
obj = Solution()
root1 = obj.insert(root)
res = obj.rangeSumBST(root1, low, high)
res1 = obj.rangeSumBSTUsingRecursion(root1, low, high)
print(res1 == res)
