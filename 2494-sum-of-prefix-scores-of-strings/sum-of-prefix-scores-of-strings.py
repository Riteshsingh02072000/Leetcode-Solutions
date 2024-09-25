class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # d = defaultdict(int)
        # for x in words:
        #     s = ""
        #     for y in x:
        #         s+=y
        #         d[s]+=1
        
        # ans = []

        # for word in words:
        #     score = 0
        #     s = ""
        #     for x in word:
        #         s+=x
        #         score+=d[s]
        #     ans.append(score)
        # return ans

        trie = self.buildTrie(words)
        return self.helper(trie, words)

    def buildTrie(self, words):
        trie ={}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})

                node['$'] = node.get('$', 0) +1
        return trie
    
    def helper(self, trie, words):
        ans = []
        for word in words:
            node = trie
            score = 0
            for char in word:
                node = node[char]
                score+=node['$']
            ans.append(score)
        return ans