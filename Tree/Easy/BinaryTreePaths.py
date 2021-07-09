# https://leetcode.com/problems/binary-tree-paths/
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root, path, res):
            if not root.left and not root.right:
                path += str(root.val)
                res.append(path)
            if root.left:
                dfs(root.left, path + str(root.val) + '->', res)
            if root.right:
                dfs(root.right, path + str(root.val) + '->', res)
            return res
        return dfs(root, '', [])


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

print(Solution().binaryTreePaths(root))
