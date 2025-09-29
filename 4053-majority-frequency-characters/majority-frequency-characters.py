class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        count = Counter(s)

        res = defaultdict(list)
        for i in count:
            res[count[i]].append(i)
        
        new = defaultdict(list)
        for i in res:
            new[len(res[i])].append(i)
        
        w = res[max(new[max(new)])]
        return ''.join(w)