class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:

        ans = fSum = iSum = 0

        for i,flip in enumerate(flips):

            fSum+= flip
            iSum+= i+1

            ans+= (iSum==fSum)

        return ans