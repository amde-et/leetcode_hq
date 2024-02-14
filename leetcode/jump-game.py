class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j=len(nums)-1

        while j>0:
            if nums[j-1]>0:
                j-=1
            else:
                i=j-1
                while nums[i]<j-i:
                    if i<=0:
                        return False
                    i-=1
                j=i
        return True