class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        adj = collections.defaultdict(list)
        n = len(beginWord)

        for word in wordList:
            for j in range(n):
                pattern = word[:j] + '*' + word[j+1:]
                adj[pattern].append(word)
        
        visited = set([beginWord])
        steps = 1
        q = deque([beginWord])

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps
                for i in range(n):
                    pattern = word[:i] + '*' + word[i+1:]
                    for adjWord in adj[pattern]:
                        if adjWord not in visited:
                            visited.add(adjWord)
                            q.append(adjWord)
            steps += 1
        return 0
        # q = deque([(beginWord, 1)])
        # visited = set()
        # n = len(beginWord)
        # while q:

        #     word, step = q.popleft()
        #     for i in range(n):
        #         for j in range(26):
        #             newWord = word[:i] + chr(97+j) + word[i+1:]
        #             if newWord == endWord:
        #                 return step+1
        #             if newWord in wordList and newWord not in visited:
        #                 q.append((newWord, step+1))
        #                 visited.add(newWord)
        # return 0