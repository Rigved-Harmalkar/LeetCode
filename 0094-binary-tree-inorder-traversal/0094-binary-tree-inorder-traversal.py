# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder_recursive(root)

    def inorder_recursive(self,node):
        if not node:
            return []
        return self.inorder_recursive(node.left) + [node.val] + self.inorder_recursive(node.right)
        