class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        my_dict = {}
        count = 0
        for i in answers:
		
            if i == 0:
                count+=1
            else:
			
                if i not in my_dict or i == my_dict[i]:
                    my_dict[i] = 0
                    count+=1 + i
                else:
                    my_dict[i]+=1
               
                    
        return count