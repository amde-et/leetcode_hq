class Solution:
    def minimumRecolors(self, b: str, k: int) -> int:
        i = 0
        l = []
        while i < len(b):
            s = b[i:i + k]
            if len(s) == k:
                l.append(s.count('W'))
            i += 1
        return min(l)