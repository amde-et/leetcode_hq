class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pv=p.val
        qv=q.val
        while(root!=None):
            if pv <root.val and qv<root.val:
                root=root.left
            elif pv>root.val and qv>root.val:
                root=root.right
            else:
                return root
        return root