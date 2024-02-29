class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        pool = tuple(range(1, n+1))
        n = len(pool)
        indices = list(range(k))
        res = [tuple(pool[i] for i in indices)]
        while True:
            for i in reversed(range(k)):
                # - Select i if i is not at its maximum
                if indices[i] != i + n - k:
                    break
            else: # Reach the last combination
                return res
            indices[i] += 1
            # - Align the indices after i 
            for j in range(i+1, k):
                indices[j] = indices[j-1] + 1
            res.append(tuple(pool[i] for i in indices))