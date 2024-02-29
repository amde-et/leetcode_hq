class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        helper = []
        self.findAns(0, target, candidates, ans, helper)
        return ans
    
    def findAns(self, index, target, arr, ans, helper):
        if index == len(arr):
            if target == 0:
                ans.append(helper[:])
            return
        
        if arr[index] <= target:
            helper.append(arr[index])
            self.findAns(index, target - arr[index], arr, ans, helper)
            helper.pop()
        
        self.findAns(index + 1, target, arr, ans, helper)