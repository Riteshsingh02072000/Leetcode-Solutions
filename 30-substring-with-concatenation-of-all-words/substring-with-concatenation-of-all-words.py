class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        
        word_length = len(words[0])
        total_length = len(words)*word_length

        word_count = collections.defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        ans = []

        for i in range(word_length):
            left = i
            count = 0
            window = collections.defaultdict(int)

            for j in range(i, len(s) - word_length+1, word_length):
                word = s[j:j+word_length]

                if word in words:
                    window[word]+=1
                    count+=1

                    while window[word]>word_count[word]:
                        left_word = s[left:left+word_length]
                        window[left_word] -=1
                        left += word_length
                        count-=1
                    
                    if count == len(words):
                        ans.append(left)
                else:
                    count = 0
                    window.clear()
                    left = j+word_length
        return ans