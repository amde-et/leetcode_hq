class Solution:
    def countGoodNumbers(self, n: int) -> int:
        '''
        ans=1
        MOD=int(10**9+7)
        for i in range(n):
            if i%2==0:
                ans*=5
            else:
                ans*=4
            ans%=MOD
        return ans
        '''
        MOD=int(10**9+7)

        fives,fours=n//2+n%2,n//2
        # 5^fives*4^fours % MOD
        # = 5^fives % MOD * 4^fours % MOD
        return (pow(5,fives,MOD) * pow(4,fours,MOD)) % MOD