class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        visited = set()

        while q:
            cur = q.popleft()
            for word in wordDict:
                if cur.startswith(word):
                    new_cur = cur[len(word):]
                    if new_cur == "":
                        return True
                    if new_cur not in visited:
                        q.append(new_cur)
                        visited.add(new_cur)
        return False