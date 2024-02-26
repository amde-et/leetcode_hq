
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def solver(l,r):
            if l>r:
                return None
            mid=(l+r)//2
            root=TreeNode(nums[mid])
            root.left=solver(l,mid-1)
            root.right=solver(mid+1,r)
            return root
        ans=solver(0,len(nums)-1)
        return ans