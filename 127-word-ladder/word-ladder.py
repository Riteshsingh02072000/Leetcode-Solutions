class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        q = deque([(beginWord, 1)])
        visited = set()
        n = len(beginWord)
        while q:

            word, step = q.popleft()
            for i in range(n):
                for j in range(26):
                    newWord = word[:i] + chr(97+j) + word[i+1:]
                    if newWord == endWord:
                        return step+1
                    if newWord in wordList and newWord not in visited:
                        q.append((newWord, step+1))
                        visited.add(newWord)
        return 0