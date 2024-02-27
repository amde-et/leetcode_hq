class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans=[]
        ans.append(deck[-1])
        for i in range(len(deck)-1):
            ans.insert(0,ans[-1]) #inserting last element
            ans.insert(0,deck[len(deck)-2-i]) #inserting last 2nd element in the process
            ans.pop() #pop the last element
        return ans