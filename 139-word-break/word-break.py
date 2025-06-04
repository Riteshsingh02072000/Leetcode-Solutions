class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        visited = set()

        while q:
            cur = q.popleft()
            for word in wordDict:
                if cur.startswith(word):
                    newCur = cur[len(word):]
                    if newCur == "":
                        return True
                    if newCur not in visited:
                        q.append(newCur)
                        visited.add(newCur)
        return False