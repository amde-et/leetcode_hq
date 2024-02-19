class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        tar = len(set(nums))
        n = len(nums)
        res=0
        for i in range(0,n-tar+1):
            aux = set(nums[i:i+tar])
            test=True
            for k in range(i+tar, n):
                if len(aux)<tar:
                    aux.add(nums[k])
                else:
                    v=n-k+1
                    res+=v
                    test=False
                    break
            if test and len(aux)>=tar:
                res+=1
        return res
        