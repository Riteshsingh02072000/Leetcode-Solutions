class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        count = Counter(s)

        first = {k:s.find(k) for k in count}
        last = {k: s.rfind(k) for k in count}

        res= []
        q = deque()

        for k in count:
            q.appendleft([first[k], last[k], count[k]])

            left, right, total = inf, -inf, 0
            for x, y, z in q:
                total += z
                left = min(x, left)
                right = max(y, right)

                if total == right - left+1:
                    break
            if total == right - left+1:
                res.append(s[left: right+1])
                q = deque()
        return res