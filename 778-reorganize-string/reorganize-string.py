class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [[-val, char] for char, val in Counter(s).items()]
        heapq.heapify(heap)
        ans = ""
        prev = None

        while heap or prev:
            if not heap and prev:
                return ''
            freq, char = heappop(heap)
            ans += char
            freq+=1
            if prev:
                heappush(heap, prev)
                prev =None
            if freq!=0:
                prev = [freq, char]
        return ans