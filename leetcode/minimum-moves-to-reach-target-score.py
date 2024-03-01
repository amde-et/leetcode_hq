class Solution:
    def minMoves(self, a: int, m: int) -> int:
        if m==0:
            return a-1
        else:
            c=0
            while a>0 and m>0:
                if a%2!=0:
                   c=c+1
                   a=a-1
                else:
                   a=a//2
                   m=m-1
                   c=c+1  
            return a+c-1