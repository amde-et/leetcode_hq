class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic={}
        tot=0
        flg=0
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i]%2==0:
                tot+=dic[i]
            else:
                flg=1
                tot+=dic[i]-1
        if flg==1:
            return tot+1
        return tot