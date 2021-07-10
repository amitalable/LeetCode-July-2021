# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []

        def dfs(root):
            if root:
                for i in range(len(root.children)):
                    dfs(root.children[i])
                self.res.append(root.val)
        dfs(root)
        return self.res
