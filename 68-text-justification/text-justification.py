class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur = []
        ans = []
        count = 0

        for word in words:
            if len(word) + count + len(cur)>maxWidth:
                size = max(1, len(cur)-1)
                for i in range(maxWidth-count):
                    index = i%size
                    cur[index] += ' '
                ans.append(''.join(cur))
                cur = []
                count = 0
            cur.append(word)
            count+=len(word)
        
        cur = ' '.join(cur)
        cur+=" "*(maxWidth-len(cur))
        print(cur)
        ans.append(cur)
        return ans