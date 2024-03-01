# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        levelMap = defaultdict(list)
        def dfs(node, level):
            if not node:
                return
            levelMap[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        # print(levelMap)
        for i, v in levelMap.items():
            if i % 2 == 0:
                res.append(v)
            else:
                res.append(v[::-1])
        return res