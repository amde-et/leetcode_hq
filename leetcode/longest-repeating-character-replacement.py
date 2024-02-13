class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ws=0
        freqmap={}
        maxlen=0
        maxfreq=0
        for we in range(len(s)):
            currchar=s[we]
            freqmap[currchar]=freqmap.get(currchar,0)+1
            maxfreq=max(maxfreq,freqmap[currchar])
            if((we-ws+1)-maxfreq > k):
                leftchar=s[ws]
                freqmap[leftchar]-=1
                if freqmap[leftchar]==0:
                    del freqmap[leftchar]
                ws+=1
            maxlen=max(maxlen,we-ws+1)
        return maxlen