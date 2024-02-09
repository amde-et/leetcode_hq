class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = [0] * 26
        pending = [0] * 26
        for c in s1:
            target[ord(c) - ord('a')] += 1
        begin, end, n, m = 0, 0, len(s2), len(s1)
        while end < n:
            c = s2[end]
            pending[ord(c) - ord('a')] += 1
            while pending[ord(c) - ord('a')] > target[ord(c) - ord('a')]:
                pending[ord(s2[begin]) - ord('a')] -= 1
                begin += 1
            end += 1
            if end - begin == m:
                return True
        return False