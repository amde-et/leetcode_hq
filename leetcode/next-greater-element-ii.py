class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, L = [], len(nums)
        res = [-1] * L

        for i in reversed(range(L * 2 - 1)):
            idx = i % L
            while stack and stack[-1] <= nums[idx]:
                stack.pop()
            res[idx] = stack[-1] if stack else -1
            stack.append(nums[idx])
        
        return res