class Solution:
    
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        minNumberShouldOccur = len(s) // 4

        def isBalanced():
            for char in 'QWER':
                if counter.get(char, 0) > minNumberShouldOccur: 
                    return False
            return True

        if isBalanced():
            return 0

        left = 0
        mini = len(s)

        
        for right, char in enumerate(s):
            counter[char] -= 1
             
            while left < len(s) and isBalanced():
                mini = min(mini, right - left + 1)
                counter[s[left]] += 1
                left += 1

        return mini

    