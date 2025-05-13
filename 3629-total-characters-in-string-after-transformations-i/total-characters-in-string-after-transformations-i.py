class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        @cache
        def helper(s, t):
            ans = 0
            for c in s:
                if ord(c) + t <= ord("z"):
                    ans += 1
                else:
                    new_t = t
                    new_t -= ord("z") + 1 - ord(c)
                    ans += helper("ab", new_t)
            return ans
        return helper(s, t) % ((10 ** 9) + 7)
