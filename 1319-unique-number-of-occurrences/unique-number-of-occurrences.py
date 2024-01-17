class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.defaultdict(int)
        for x in arr:
            count[x] +=1
        
        seen = set()
        for x in count.values():
            if x in seen:
                return False
            seen.add(x)
        return True