class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        med=0
        msf=-99999
        for i in range(0,len(nums)):
            med=med+nums[i]
            if(med<nums[i]):
                med=nums[i]
            if(msf<med):
                msf=med
        return msf
        

        