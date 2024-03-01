class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        sol = ""
        for i in range(len(s)):
            for ii in range(i+1, len(s)+1):
                if all(s[k].swapcase() in s[i:ii] for k in range(i, ii)): 
                    sol = max(sol, s[i:ii], key=len)
        return sol 