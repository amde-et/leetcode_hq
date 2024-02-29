class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n, l, r, d = len(cards), 0, 1, {}
        ans = 1000000
        d[cards[0]] = 0
        while r<n:
            while r < n and cards[r] not in d:
                d[cards[r]] = r
                r += 1
            if r == n: break
            ans = min(ans, r-d[cards[r]]+1)
            temp = d[cards[r]]+1
            for i in range(l, temp): del(d[cards[i]])
            l=temp
            d[cards[r]] = r
            r += 1

        return -1 if ans == 1000000 else ans