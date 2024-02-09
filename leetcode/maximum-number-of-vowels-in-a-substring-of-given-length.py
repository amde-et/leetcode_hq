class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        count= 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxCount = 0

        for r in range(k):
            if s[r] in vowels:
                count += 1
        maxCount = max(maxCount, count)

        r = k
        while r < len(s):
            if s[r] in vowels:
                count += 1
            if s[l] in vowels:
                count -= 1
            maxCount = max(maxCount, count)
            l += 1
            r += 1 
        return maxCount