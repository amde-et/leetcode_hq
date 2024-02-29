class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, maxi, mini):
            if node is None:
                return
            if node.val < mini:
                mini = node.val
            elif node.val > maxi:
                maxi = node.val
            nonlocal ans
            ans = max(ans, abs(maxi - mini))
            dfs(node.left, maxi, mini)
            dfs(node.right, maxi, mini)

        dfs(root, root.val, root.val)
        return ans