class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = 0
        count_10 = 0

        for i in bills:
            if i == 5:
                count_5+=1
            elif i == 10:
                count_10+=1
                count_5-=1
            elif i == 20:
                if count_10 > 0:
                    count_10-=1
                    count_5-=1
                else:
                    count_5-=3
            
            if count_5<0:
                return False
        return True

        