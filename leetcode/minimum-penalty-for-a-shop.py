class Solution:
    def bestClosingTime(self, A: str) -> int:
        A = [A.count("Y")] + list(A)
        for i in range(1, len(A)):
            A[i] = A[i - 1] + (-1)**(A[i] == "Y")
        return A.index(min(A))