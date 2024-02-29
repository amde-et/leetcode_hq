# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [root.left, root.right]
        while stack:
            node1,node2 = stack.pop(), stack.pop()
            if node1 is None and node2 is None: continue
            elif (node1 is None or node2 is None) or node1.val != node2.val: 
                return False

            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)
        return True