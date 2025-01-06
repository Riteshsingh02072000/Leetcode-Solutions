class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split('*')
        n = len(s)
        p_len, s_len = len(prefix), len(suffix)

        p_found = True if len(prefix) == 0 else False
        s_found = True if len(suffix) == 0 else False

        i = 0
        while i<n-s_len+1:
            if not p_found and s[i:i+p_len] == prefix:
                p_found = True
                i+=p_len
                continue
            elif p_found and s[i:i+s_len] == suffix:
                s_found = True
                break
            i+=1
        return p_found and s_found