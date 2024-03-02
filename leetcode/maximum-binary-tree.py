# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return 
        maximum = max(nums)
        
        index_max = nums.index(maximum)
        root = TreeNode(maximum)
        root.left = self.constructMaximumBinaryTree(nums[:index_max])
        root.right = self.constructMaximumBinaryTree(nums[index_max+1:])
        return root
        