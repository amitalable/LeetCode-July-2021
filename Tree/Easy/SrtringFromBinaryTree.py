# https://leetcode.com/problems/construct-string-from-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        str_temp = ""
        if root:
            str_temp = str(root.val)
            if root.right:
                str_temp += '('+self.tree2str(root.left)+')' + \
                    '('+self.tree2str(root.right)+')'
            elif root.left:
                str_temp += '('+self.tree2str(root.left)+')'
        return str_temp
