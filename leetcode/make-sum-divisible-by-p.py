class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        main_sum = sum(nums)
        reminder = main_sum % p

        if reminder == 0:
            return 0

        pfxrem = 0
        rightmost_rem = {0: -1}
        ans = len(nums)
        for i, v in enumerate(nums):

            pfxrem = (pfxrem + v) % p

            r = (pfxrem - reminder) % p

            if r in rightmost_rem:
                j = rightmost_rem[r]
                ans = min(ans, i - j)
            rightmost_rem[pfxrem] = i

        return ans if ans < len(nums) else -1