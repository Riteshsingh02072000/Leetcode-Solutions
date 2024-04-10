class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        ans = []
        for i in deck:
            ans = [i] + ans[-1:] + ans[:-1]
        return ans