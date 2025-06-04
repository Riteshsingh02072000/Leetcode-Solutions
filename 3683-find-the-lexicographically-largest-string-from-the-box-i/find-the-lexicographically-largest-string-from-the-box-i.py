class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        length = n-numFriends+1
        maxChar = max(word)
        ans = ""

        for i in range(n):
            if word[i] == maxChar:
                substr = word[i:i+length]
                ans = max(ans, substr)
        return ans