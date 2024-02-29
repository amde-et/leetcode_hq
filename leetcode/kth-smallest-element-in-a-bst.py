# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        preorder = []
        
        def myfucntion(node : TreeNode):
            if not(node) : return
            

            myfucntion(node.left)
            preorder.append(node.val)
            myfucntion(node.right)

        myfucntion(root)
        
        return preorder[k-1]