class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hsh = {}
        for i,char in enumerate(s):
            if char in hsh:
                hsh[char].append(i)
            else:
                hsh[char] = [i]
    
        out = []
        left,right = None,None
        for key in hsh:
            if left is None:
                left = hsh[key][0]
                right = hsh[key][-1]
            elif hsh[key][0]>right:
                out.append(right-left+1)
                left = hsh[key][0]
                right = hsh[key][-1]
            
            else:
                right = max(right,hsh[key][-1])
        out.append(right-left+1)
        return out
        