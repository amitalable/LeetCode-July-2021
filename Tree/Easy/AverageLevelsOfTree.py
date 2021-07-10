# https://leetcode.com/problems/average-of-levels-in-binary-tree/
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return None

        queue = [root]
        level = []
        next_level = []
        res = []

        while queue:
            for node in queue:
                level.append(node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

                # Append the average of each level
            res.append(sum(level) / len(level))

            queue = next_level
            next_level = []
            level = []

        return res


root = TreeNode(0)
root.left = TreeNode(14)
root.left.right = TreeNode(9)
obj = Solution()
print(obj.averageOfLevels(root))
