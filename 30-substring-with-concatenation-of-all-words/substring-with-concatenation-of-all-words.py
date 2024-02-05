class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        word_len = len(words[0])
        word_count = defaultdict(int)

        for word in words:
            word_count[word] += 1
        
        ans = []

        for i in range(word_len):
            window = defaultdict(int)
            left = i
            count = 0

            for j in range(i, len(s)-word_len+1, word_len):
                word = s[j:j+word_len]

                if word in words:
                    window[word] +=1
                    count +=1

                    while window[word]>word_count[word]:
                        left_word = s[left:left+word_len]
                        window[left_word] -= 1
                        count -= 1
                        left+= word_len
                    
                    if count==len(words):
                        ans.append(left)
                else:
                    count = 0
                    window.clear()
                    left = j + word_len
        return ans