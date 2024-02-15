class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        
        x = y = 0
        
        for i in s:
            if(i == '('):
                x += 1
            else:
                x -= 1
            
            if(x < 0):
                count += 1
                x = 0
            if(y < 0):
                count += 1
                y = 0
        
        return count + x + y