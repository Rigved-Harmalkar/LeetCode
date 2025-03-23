# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preorder_recursive(root)

    def preorder_recursive(self,node):
        if not node:
            return []
        return [node.val] + self.preorder_recursive(node.left) + self.preorder_recursive(node.right)
        