# https://leetcode.com/problems/diameter-of-binary-tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = []

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            l = dfs(node.left)  # max depth of node.left
            r = dfs(node.right)  # max depth of node.right
            ans.append(l + r)  # array for paths of each root
            return 1 + max(l, r)
        dfs(root)
        return max(ans)
