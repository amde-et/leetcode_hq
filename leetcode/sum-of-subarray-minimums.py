class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        ngel = []

        nger = []

        left = [-1 for _ in range(len(arr))]
        right = [-1 for _ in range(len(arr))]

        for i in range(len(arr)):
            l = -1
            while ngel and arr[ngel[-1]] >= arr[i]:
                ngel.pop()
            
            if ngel:
                l = ngel[-1]

            left[i] = i - l -1
            ngel.append(i)
        
        for i in range(len(arr)-1,-1,-1):
            r = len(arr)

            while nger and arr[nger[-1]] > arr[i]:
                nger.pop()
            
            if nger:
                r = nger[-1]
            
            right[i] = r - i - 1
            nger.append(i)

        ans = 0
        for i in range(len(arr)):
            ans += (left[i]*right[i]+1+left[i]+right[i])*arr[i]
            
        return ans % (10**9+7)