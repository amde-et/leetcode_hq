class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s = 0
        ans = 0
        for i in range(len(nums)):
            s = s+nums[i]
            avg = s/(i+1)
            if avg > ans:
                ans = avg
        return ceil(ans)