class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        freq = [0]*26
        for l in letters:
            freq[ord(l)-ord('a')] += 1
        
        def dfs(letterCount, index):
            if index == len(words):
                return 0
            
            skipScore = dfs(letterCount, index+1)
            wordScore = 0
            newLetterCount = letterCount[:]
            valid = True

            for c in words[index]:
                if newLetterCount[ord(c)-ord('a')]==0:
                    valid = False
                    break
                
                newLetterCount[ord(c)-ord('a')]-=1
                wordScore += score[ord(c)-ord('a')]
            takeScore = 0
            if valid:
                takeScore = wordScore + dfs(newLetterCount, index+1)
            
            return max(skipScore, takeScore)
        
        return dfs(freq, 0)
