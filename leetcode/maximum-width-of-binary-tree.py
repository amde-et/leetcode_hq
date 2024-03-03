# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [[root, 1]]
        level = 1
        num = 1
        prev_lvl = 1
        max_breadth = 0
        while q:
            max_breadth = max(q[-1][1]-q[0][1] + 1, max_breadth)
            for _ in range(len(q)):
                curr, num = q.pop(0)
                if curr.left:
                    q.append([curr.left, num*2])
                if curr.right:
                    q.append([curr.right, num*2+1])

        return max_breadth
                







