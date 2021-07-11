# https://leetcode.com/problems/maximum-depth-of-n-ary-tree
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        depth = 0
        for child in root.children:
            child_depth = self.maxDepth(child)
            if child_depth > depth:
                depth = child_depth

        return depth + 1

    def maxDepthUsingRecursion(self, root: 'Node') -> str:
        if root:
            return 1 + (max([self.maxDepthUsingRecursion(node) for node in root.children])
                        if root.children else 0)
        return 0
