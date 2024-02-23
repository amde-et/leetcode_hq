class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = [0]

        for i in range(len(s)):
            if s[i] == '(':
                score.append(0)
            else:
                last_score = score.pop()
                if last_score == 0:
                    score[-1] += 1
                else:
                    score[-1] += 2*last_score
        
        return score[0]

