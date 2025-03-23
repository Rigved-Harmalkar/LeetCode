# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorder_recursive(root)

    def postorder_recursive(self,node):
        if not node:
            return []
        return self.postorder_recursive(node.left) + self.postorder_recursive(node.right) + [node.val]
        