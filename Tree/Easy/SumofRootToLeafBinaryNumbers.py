# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return
        self.res = 0

        def dfs(root, s):
            if not root:
                return
            s += str(root.val)
            if not root.left and not root.right:
                self.res += int(s, 2)
                s = s[:-1]
            if root.left:
                dfs(root.left, s)
            if root.right:
                dfs(root.right, s)
        dfs(root, "")
        return self.res


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print(Solution().sumRootToLeaf(root))
