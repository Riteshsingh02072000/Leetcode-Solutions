class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        char = sorted(s, reverse = True)
        ans = []
        freq = 1
        idx = 0

        for i in range(len(char)):
            if ans and ans[-1] == char[i]:
                if freq<repeatLimit:
                    ans.append(char[i])
                    freq += 1
                else:
                    idx = max(idx, i+1)
                    while idx<len(char) and char[idx] == char[i]:
                        idx+=1
                    if idx<len(char):
                        ans.append(char[idx])
                        char[i], char[idx] = char[idx], char[i]
                        freq = 1
                    else:
                        break

                
            else:
                ans.append(char[i])
                freq = 1
        return ''.join(ans)
