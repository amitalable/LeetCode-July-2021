class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        stack1 = [root1]
        stack2 = [root2]
        while stack1 and stack2:
            if self.getNextLeaf(stack1).val != self.getNextLeaf(stack2).val:
                return False
        return not stack1 and not stack2

    def getNextLeaf(self, stack):
        curr = stack.pop()
        while curr.left or curr.right:
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            curr = stack.pop()
        return curr

#     def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
#         def dfs(root,res):
#             if root:
#                 dfs(root.left,res)
#                 if not root.left and not root.right:
#                     res.append(root.val)
#                     return res
#                 dfs(root.right,res)
#             return res
#         return dfs(root1,[]) == dfs(root2,[])
