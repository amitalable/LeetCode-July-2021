# https://leetcode.com/problems/n-ary-tree-preorder-traversal
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []

        def dfs(root):
            if root:
                self.res.append(root.val)
                for i in range(len(root.children)):
                    dfs(root.children[i])
        dfs(root)
        return self.res
